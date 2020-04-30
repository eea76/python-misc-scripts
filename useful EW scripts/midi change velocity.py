# This script looks at midi files in a directory and
# changes matching velocities to another specified value.

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
                            if velocity + 20 > 127:
                                events.set_velocity(127)
                            else:
                                events.set_velocity(velocity + 20)
                                              
                        changed = True
            if changed:
                #midi.write_midifile(path + "NEW_VEL " + file, pattern)
                #midi.write_midifile(fullpath, pattern)
                changed_count += 1


print "Done."
print "%d files were changed out of %d files total." % (changed_count, file_count)