# This script looks at midi files in a directory and
# finds specified notes (midi note numbers).

import midi, os
from midi import *

path = raw_input("Enter path: ")
file_count = 0
changed_count = 0
deleted_notes = 0
count = 0

high_list = []

for root, dirs, files in os.walk(path):
    for file in files:
        fullpath = os.path.join(root, file)
        if file.endswith(".mid"):
            file_count += 1
            changed = False
            in_transformed = False
            found = False
            pattern = midi.read_midifile(fullpath)
            for track in pattern:
                for events in track:
                    if events.name == "Note On":
                        note = events.get_pitch()
                        if note > 82:
                            #print "fix this or whatever"
                            found = True
                            events.set_velocity(0)
            if found:
                count += 1
                print fullpath
                midi.write_midifile(fullpath, pattern)





print "Done."
print "%d files were found out of %d files total." % (count, file_count)