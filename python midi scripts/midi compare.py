import midi, os, sys
from midi import *

extension = raw_input("Enter the file extension: ")

#new_path = raw_input("Enter the NEW path to search in: ")
new_path = "/Users/elon/Desktop/python midi scripts/midis/midi grooves 6-23-14 NewFileStructure wFills"
legacy_list = []
#legacy_path = raw_input("Enter the LEGACY path to search in: ")
legacy_path = "/Users/elon/Desktop/python midi scripts/midis/midi grooves 6-23-14 LegacyFile Structure wFills"
file_count = 0  
found_list = []
new_list = []

for root, dirs, files in os.walk(new_path):
    for file in files:
        fullpath = os.path.join(root, file)
        if file.endswith(extension):
            file_count += 1
            new_list.append(file)

print file_count
file_count = 0
for root, dirs, files in os.walk(legacy_path):
    for file in files:
        fullpath = os.path.join(root, file)
        if file.endswith(extension):
            file_count += 1
            legacy_list.append(file)

print "NEW:", len(new_list)
print "LEGACY:", len(legacy_list)

print file_count
print new_list

for midifile in legacy_list:
    if midifile in new_list:
        new_list.remove(midifile)

for x in new_list:
    print x


#new_list = set(new_list)
#legacy_list = set(legacy_list)

#print new_list - legacy_list

def list_difference(new_list, legacy_list):
    """uses legacy_list as the reference, returns list of items not in new_list"""
    diff_list = []
    for item in legacy_list:
        if not item in new_list:
            diff_list.append(item)
    return diff_list

#print len(list_difference(legacy_list, new_list))