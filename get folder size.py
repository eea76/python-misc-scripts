import os, sys, shutil

path = input("Enter the full path: ")
if not path.endswith("/"):
    path += "/"
totalsize = 0
filecount = 0

for library in os.listdir(path):
    if not os.path.isdir(path + library): continue # <-- saying if the filename is not a directory, SKIP that iteration
    librarysize = 0
    for root, dirs, files in os.walk(path + library):
       os.chdir(root) # sets the current iterated directory; all relatives are relative to this path
       for file in files:
              librarysize += os.path.getsize(file)
              filecount += 1
    totalsize += librarysize

print("Total size is %d bytes (%.2fMB)" % (totalsize, float((totalsize / 1000000))))
print("%d files found." % filecount)
