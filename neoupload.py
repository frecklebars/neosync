import os, sys
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

alldirs = []

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

if __name__ == "__main__":
    check_leaf(folder)
    #nc.upload(*alldirs)
    print(alldirs)
    print("done!")
