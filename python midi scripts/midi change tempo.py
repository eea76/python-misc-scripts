# This script looks at midi files in a directory and
# changes their tempos based on the tempo listed in its filename,
# given the following naming pattern: BE 085 Brothers Chorus Ride.mid

import midi, os
from midi import *

path = raw_input("Enter path: ")
file_count = 0
changed_count = 0

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
                    if events.name == "Set Tempo":
                        current_tempo = events.get_bpm()
                        new_tempo = int(file.split(" ")[1])
                       
                        if new_tempo != int(current_tempo):
                            print file
                            print "OLD:", current_tempo
                            events.set_bpm(new_tempo)
                            changed = True
                            print
                            
                        #print current_tempo
                        #print new_tempo

            if changed:
                midi.write_midifile(fullpath, pattern)
                #midi.write_midifile(path + "new " + file, pattern)
                changed_count += 1 

print "Done."
#print "%d files were found out of %d files total." % (deleted_notes, file_count)