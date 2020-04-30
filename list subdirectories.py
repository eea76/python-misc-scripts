# This script lists subdirectories in a supplied parent directory.

import os, sys, shutil

path = input("Enter a path: ")

for library in os.listdir(path):

    if not ("." in library):
        for root, dirs, files in os.walk(path + library):
            for file in files:
            	print(file + " :D")
            for name in dirs:
                print(name)
    #print(library)

