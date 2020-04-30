import midi, os
from midi import *


path = "/Users/elon/Desktop/FINAL midis for jay/congas/Jazz Congas copy 2"
file_count = 0
changed_count = 0
for root, dirs, files in os.walk(path):
    for file in files:
        fullpath = os.path.join(root, file)
        if file.endswith(".mid"):
            file_count += 1
            changed = False
            pattern = midi.read_midifile(fullpath)
            #print pattern
            for track in pattern:
                for events in track:
                    if events.name == 'Track Name':
                        print "OLD: ", events.text,
                        print fullpath
                        events.text = file[:-4]
                        events.data = [ord(ch) for ch in events.text]
                        print "NEW: ", events.text
                        changed = True
            if changed:
                midi.write_midifile(fullpath, pattern)
                #midi.write_midifile(path + "new " + file, pattern)
                changed_count += 1 


print "Done."
print "%d files were changed out of %d files total." % (changed_count, file_count)

