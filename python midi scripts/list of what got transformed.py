# This script looks at midi files in a directory and
# changes matching velocities to another specified value.

import midi, os
from midi import *

path = "/Users/elon/Desktop/python midi scripts/4midi grooves transformed"
file_count = 0
changed_count = 0
deleted_notes = 0
transformed = [ 43,
                44,
                47,
                48,
                49,
                50,
                52,
                53,
                55,
                57
                ]

trans_list = []

for root, dirs, files in os.walk(path):
    for file in files:
        fullpath = os.path.join(root, file)
        if file.endswith(".mid"):
            file_count += 1
            changed = False
            in_transformed = False
            pattern = midi.read_midifile(fullpath)
            for track in pattern:
                for events in track:
                    if events.name == "Note On":
                        note = events.get_pitch()
                        if note in transformed:
                            trans_list.append(str(note) + ": " + fullpath)
                            
#print trans_list
print len(trans_list)
trans_list.sort()
print len(set(trans_list))
my_set = set(trans_list)
fuck_you = list(my_set)
fuck_you.sort()
crazy = open("list of transformed.txt", "w")
for x in fuck_you:
    crazy.write(x+"\n")
crazy.close()

print "Done."
print "%d files were deleted out of %d files total." % (deleted_notes, file_count)