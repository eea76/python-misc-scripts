# This script looks at midi files in a directory and
# retrieves each file's time signature.

import midi, os
from midi import *

path = raw_input("Enter path: ")
file_count = 0

for root, dirs, files in os.walk(path):
    for file in files:
        fullpath = os.path.join(root, file)
        if file.endswith(".mid"):
            file_count += 1

            pattern = midi.read_midifile(fullpath)
            for track in pattern:
                for events in track:
                    if events.name == "Time Signature":
                        top = events.get_numerator()
                        bottom = events.get_denominator()
                        print file
                        print "TOP NUMBER:", top
                        print "BOTTOM NUMBER:", bottom
                        print
print "Done."
print "%d files were found." % file_count