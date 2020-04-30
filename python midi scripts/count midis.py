import midi, os, sys
from midi import *

path = raw_input("Enter the path to search in: ")
extension = raw_input("Enter the file extension: ")
file_count = 0
found_list = []

for root, dirs, files in os.walk(path):
    for file in files:
        fullpath = os.path.join(root, file)
        if file.endswith(extension):
            file_count += 1
            found_list.append(file)

no_dupes = set(found_list)

print "\nTotal %s files: %s" % (extension, file_count)
print "UNIQUE %s files: %s" % (extension, len(no_dupes))