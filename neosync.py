#!/usr/bin/python

import argparse
import os, json
from neocities import NeoCities

os.chdir(os.path.dirname(os.path.realpath(__file__)))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("website", type=str, metavar="WEBSITE")
    parser.add_argument("-d", "--dry", action="store_false", dest="dry", help="dry run")
    parser.add_argument("-v", "--verbose", action="store_true", dest="verbose", help="verbose")
    args = parser.parse_args()

    website = args.website
    wet = args.dry
    verbose = args.verbose

    if not wet: print("DRY RUN")

    with open("websites", "r") as f:
        websites = json.load(f)

    if website not in websites:
        print("website info not found")
        return

    website = websites[website]
    del(websites)

    if website["path"][-1] != "/":
        website["path"] = website["path"] + "/"

    nc = NeoCities(website["user"], website["pass"])
    
    localfiles = []
    for path, dirs, files in os.walk(website["path"]):
        for file in files:
            localfiles.append(os.path.join(path, file))
    
    if verbose: print(f"found {len(localfiles)} local files")

    nclist = nc.listitems()
    if nclist["result"] != "success":
        print("failed listing website items")
        return
    
    if verbose: print("fetched site files list")

    nclist = nclist["files"]
    sitefiles = []
    for file in nclist:
        if not file["is_directory"]:
            sitefiles.append(file["path"])

    if verbose: print(f"found {len(sitefiles)} site files")

    sitefiles.sort()
    localfiles.sort()

    rmfiles = []
    addfiles = []

    # get files to delete
    for sf in sitefiles:
        if not os.path.join(website["path"], sf) in localfiles:
            rmfiles.append(sf)

    if verbose: print(f"{len(rmfiles)} files to remove")
    
    for lf in localfiles:
        addfiles.append((lf, lf.replace(website["path"], "")))
    
    if len(rmfiles) > 0:
        if verbose: print("deleting files")
        if wet: nc.delete(*rmfiles)

    ###############
    # for some reason uploading throws an error here, even if deleting """works"""
    # it only works when using username and password, when trying with an api
    # token it throws a "method not found" error or something like that
    # cant be bothered to try again to check

    # in any case, this is still useful for deleting
    # TODO idk fix it? dont really care _that_ much
    # i guess i could just do an upload with the actual api using requests
    #
    # but do i care? at this point i can just write a shell script using their cli tool
    # which works
    ###############

    # if verbose: print("uploading files")
    # if wet: nc.upload(*addfiles)

    print("finished")

if __name__ == "__main__":
    main()
