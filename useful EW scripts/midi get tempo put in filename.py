import midi, os
from midi import *

path = "/Users/elon/Desktop/tempos/"
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
                    if events.name == "Set Tempo":
                        current_temp = events.get_bpm()
                        #print events.get_bpm()
                        changed = True

            if changed:
                temp = int(current_temp)
                file_parts = file.split(" ")
                file_parts.insert(0, str(temp))
                fixed_filename = ' '.join(file_parts)

                file_dir = os.path.dirname(fullpath) + "/"
                print "OLD: ", file
                print "NEW: ", fixed_filename
                os.rename(fullpath, file_dir + fixed_filename)
                
                changed_count += 1 

print "Done."
print "%d files were changed out of %d files total." % (changed_count, file_count)
