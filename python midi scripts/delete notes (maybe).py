
import midi, os
from midi import *

path = "/Users/elon/Desktop/python midi scripts/midis/midi grooves 7-11-14 copy 2"
file_count = 0
changed_count = 0
#bad_note = [75, 64, 54, 61, 62, 63, 65, 58, 50, 66, 60, 52, 55, 56, 76, 77, 80, 81, 87, 67, 68]
for root, dirs, files in os.walk(path):
    for file in files:
        fullpath = os.path.join(root, file)
        if file.endswith(".mid"):
            file_count += 1
            changed = False
            pattern = midi.read_midifile(fullpath)
            for track in pattern:
                for events in track:
                    if events.name == "Note On":
                        if events.get_pitch() > 82:
                            events.set_velocity(0)
                                              
                        changed = True
            if changed:
                midi.write_midifile(path + "NEW " + file, pattern)
                #midi.write_midifile(fullpath, pattern)
                changed_count += 1


print "Done."
print "%d files were changed out of %d files total." % (changed_count, file_count)