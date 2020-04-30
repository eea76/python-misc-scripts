# This script looks at a path and gets the sizes of the 
# contents inside it.


import os, sys

path = raw_input("Enter path: ")
total_size = 0

for folder in os.listdir(path):
    if not os.path.isdir(os.path.join(path, folder)):
        root_files_size = 0
        file_path = os.path.join(path, folder)
        root_files_size += os.path.getsize(file_path)
        sys.stdout.write(folder + ": ")
        if root_files_size > 0 and root_files_size < 1000:
            print "%d B" % root_files_size
        elif root_files_size >= 1000 and root_files_size < (1000**2):
            print "%d KB" % (root_files_size / 1000.0)
        elif root_files_size >= (1000**2) and root_files_size < (1000**3):
            print "%.2f MB" % (root_files_size / (1000.0**2))
        elif root_files_size >= 1000**3:
            print "%.2f GB" % (root_files_size / (1000.0**3)) 
        continue

    sys.stdout.write(folder + ": ")
    size = 0

    for root, dirs, files in os.walk(os.path.join(path, folder)):
        for name in files:
            fullpath = os.path.join(root, name)
            size += os.path.getsize(fullpath)

    total_size += size
   
    if size < (1000**2):
        print "%d KB" % (size / 1000.0)
    elif size >= (1000**2) and size < (1000**3):
        print "%.2f MB" % (size / (1000.0**2))
    elif size >= 1000**3:
        print "%.2f GB" % (size / (1000.0**3))

if total_size + root_files_size < (1000**2):
    print "\nTotal: %d KB" % ((total_size / 1000.0) + (root_files_size / 1000.0))
elif total_size + root_files_size >= (1000**2) and total_size < (1000**3):
    print "\nTotal: %.2f MB" % ((total_size / (1000.0**2)) + (root_files_size / (1000.0**2)))
elif total_size + root_files_size >= 1000**3:
    print "\nTotal: %.2f GB" % ((total_size / (1000.0**3)) + (root_files_size / (1000.0**3)))