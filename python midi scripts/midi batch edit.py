import midi, os
from midi import *

GM_Dict = {
                43 : 41,
                47 : 43,
                48 : 45,
                50 : 45

                }

'''GM_Dict = {
                39: 37,
                43: 41,
                44: 34,
                47: 43,
                48: 45,
                49: 54,
                50: 45,
                52: 56,
                53: 51,
                54: 34,
                55: 56,
                56: 51,
                57: 56,
                58: 54,
                59: 52,
                60: 45,
                61: 43,
                62: 43,
                63: 43,
                64: 41,
                65: 43,
                66: 45,
                67: 51,
                68: 51,
                75: 37,
                76: 51,
                77: 51,
                80: 51,
                81: 51,
                87: 51
                }'''

path = "/Users/elon/Desktop/python midi scripts/toms transform "
file_count = 0
changed_count = 0
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
                        note = events.get_pitch()
                        for key, value in GM_Dict.items():
                            if note == key:
                                #print "Matched note %s with dictionary key %s" % (str(note), str(key))
                                #print "Replacing note %s with note %s" % (str(key), str(value))
                                events.set_pitch(value)
                                changed = True
            if changed:
                midi.write_midifile(fullpath, pattern)
                #print fullpath
                changed_count += 1


print "Done."
print "%d files were changed out of %d files total." % (changed_count, file_count)