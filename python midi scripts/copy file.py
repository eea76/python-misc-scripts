import os, shutil

path = raw_input("Enter path: ")

for root, dirs, files in os.walk(path):
    for name in files:
        fullpath = os.path.join(root, name)
        shutil.copy(fullpath, "/Users/elon/Desktop/python midi scripts/old/new2")