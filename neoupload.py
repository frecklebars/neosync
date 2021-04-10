import os, sys, pickle
import neocities

###### CONFIG ######
username = ""
password = ""
folder = ""
####################

if len(sys.argv) > 1:
    username = sys.argv[1]
    password = sys.argv[2]
    folder = sys.argv[3]

nc = neocities.NeoCities(username, password)

try:
    with open("prevdirs.pkl", "rb") as f:
        prevdirs = pickle.load(f)
except:
    prevdirs = []

alldirs = []
deldirs = []

def check_leaf(folder_path):
    dirlist = os.listdir(folder_path)

    for d in dirlist:
        if not "." in d:
            check_leaf(os.path.join(folder_path, d))
        else:
            filepath = os.path.join(folder_path, d)
            filepath = filepath.replace("\\", "/")
            filepath2 = filepath.removeprefix(folder + "/")
            alldirs.append((filepath, filepath2))

def compare(alldirs, prevdirs):
    for t in prevdirs:
        if t not in alldirs:
            deldirs.append(t[1])

if __name__ == "__main__":
    check_leaf(folder)
    compare(alldirs, prevdirs)
    
    nc.delete(*deldirs)
    nc.upload(*alldirs)

    with open("prevdirs.pkl", "wb") as f:
        pickle.dump(alldirs, f)

    print("done!")
