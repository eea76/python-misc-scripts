# This script looks at midi files in a directory and
# adds the time signature to the filename

import midi, os
from midi import *

path = raw_input("Enter the path name: ")
found_count = 0
file_count = 0
changed_count = 0
print "\nWhat time signature do you want to add (4/4, 3/4, etc)?\n"
ts = raw_input("Please use '-'' instead of '/': ")

for root, dirs, files in os.walk(path):
    for file in files:
        fullpath = os.path.join(root, file)
        if file.endswith(".mid"):
            file_count += 1
            changed = False
            found = False
            pattern = midi.read_midifile(fullpath)
            for track in pattern:
                for events in track:
                    if events.name == "Time Signature":
                        top = events.get_numerator()

                        bottom = events.get_denominator()

                        splitfile = file.split(" ")
                        if splitfile[2] != str(top) + "-" + str(bottom):
                            found_count += 1
                            print fullpath[73:]
                            print str(top) + "-" + str(bottom)
                            print
                        #print top, bottom
                        #print ts.split("-")[0], ts.split("-")[1]
                        #print'''
                        if top == int(ts.split("-")[0]) and bottom == int(ts.split("-")[1]):
                            found = True
                           
            if found:
                if ts not in file:
                    splitfile = file.split(" ")
                    splitfile.insert(2, ts)
                    newfile = " ".join(splitfile)
                    
                    changed_count += 1
                    file_dir = os.path.dirname(fullpath)
                    os.rename(fullpath, file_dir + "/" + newfile)
                    print fullpath

print "Done."
print found_count
print "%d files were changed out of %d files total." % (changed_count, file_count)