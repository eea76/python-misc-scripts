# This script looks at a path and lists all its files
# and folders recursively, and formats it according to
# its folder structure

# Basically mirrors OS X's expanded tree view in Finder
# Also it will count specific file types.

import os, sys, shutil
count = 0

path = input("Enter path: ")

def walkdir(path, indent = 0):
    global count
    files = os.listdir(path)
    for f in files:
        fullpath = ("%s/%s" % (path, f))
        print(' ' * indent + f)
        if fullpath.endswith(".mid"):
            count += 1
        if os.path.isdir(fullpath):
            walkdir(fullpath, indent + 4)

walkdir(path)

print(count)