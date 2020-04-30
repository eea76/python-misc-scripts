# This script looks at midi files in a directory and
# analyzes their velocities.

import midi, os
from midi import *

path = "/Users/elon/Desktop/midi grooves/Big Easy/Fills/095 Secondline 2 Fills/"
file_count = 0
changed_count = 0
snare_list = []
under_100 = 0
over_100 = 0
for root, dirs, files in os.walk(path):
    for file in files:
        fullpath = os.path.join(root, file)
        if file.endswith(".mid"):
            file_count += 1
            changed = False
            pattern = midi.read_midifile(fullpath)
            #print "\n----" + file + "----\n"
            for track in pattern:
                for events in track:
                    if events.name == "Note On":
                        note = events.get_pitch()
                        velocity = events.get_velocity()
                        if note == 38 and velocity > 0:
                            snare_list.append(velocity)

        for snare in snare_list:
            if snare >= 100:
                over_100 += 1
            else:
                under_100 += 1

        if over_100 > 0:
            print file, "%s out of %s snares are under 100" % (under_100, len(snare_list))


        over_100 = 0
        under_100 = 0
        snare_list = []


print "Done."
print "%d files were changed out of %d files total." % (changed_count, file_count)