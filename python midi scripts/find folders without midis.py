import midi, os, sys
from midi import *

path = raw_input("Enter the path to search in: ")
before_count = 0
after_count = 0
found_count = 0
found_list = []
total_size = 0

for root, dirs, files in os.walk(path):
    for f in files:
        before_count += 1

for root, dirs, files in os.walk(path):
    for f in files:
        fullpath = os.path.abspath(os.path.join(root, f))
        if fullpath.endswith(".DS_STORE") or fullpath.endswith(".pm"):
            print fullpath
            total_size += os.path.getsize(fullpath)
            found_list.append(fullpath)
            os.remove(fullpath)
            found_count += 1

for root, dirs, files in os.walk(path):
    for f in files:
        after_count += 1

my_set = set()

for extension in found_list:
    my_set.add(extension.split(".")[1])

#print len(my_set), "different file types"
#for x in my_set:
#    print x

print "Before: %s" % before_count
print "After: %s" % after_count
print "Total file size is %s bytes." % total_size
print "Deleted %s files." % found_count