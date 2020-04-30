#This program finds files of a given extension from directory (recursive)
#and lists them all in a flattened list.
#In other words it goes all the way down and
#finds files as deep as it can, and then lists
#them all out.


import shutil, os, time
source = input("Enter source path: ")
if not source.endswith("/"):
    source += "/"
extension = input("Enter a file extension to search for: ")

starttime = time.time()
print("Running. Please wait...")

found = 0

for root, dirs, files, in os.walk(source):
    for name in files:
        fullpath = os.path.join(root, name) # creates the fullpath to the file
        if name.endswith(extension):
            found += 1
            print(fullpath)
            #title = name.title()
            #print(title.split('.')[0])

elapsedtime = time.time() - starttime

print("All done. Copy operation took %sm and %ss" % (int(elapsedtime//60), int(elapsedtime % 60)))
print("%d %s files found." % (found, extension))
