
import midi, os
from midi import *

path = "/Users/elon/Desktop/python midi scripts/3midi grooves GM deleted aux files"
file_count = 0
changed_count = 0
deleted_notes = 0
'''bad_note =  {
            39: "Hand Clap",
            75: "Claves",
            43: "Floor Tom High", 
            64: "Conga Low", 
            44: "Hi Hat Pedal", 
            54: "Tambourine", 
            47: "Rack Tom Low Mid", 
            61: "Bongo Low", 
            62: "Conga Hi Mute", 
            63: "Conga Hi Open", 
            65: "Timbale Hi", 
            48: "Rack Tom Hi Mid", 
            50: "Rack Tom Hi", 
            60: "Bongo Hi", 
            66: "Timbale Low", 
            49: "Cymbal Crash 1",
            58: "Vibraslap (lol)", 
            52: "Cymbal Chinese", 
            55: "Cymbal Splash", 
            57: "Cymbal Crash 2", 
            53: "Ride Bell", 
            56: "Cowbell", 
            67: "Agogo Hi", 
            68: "Agogo Low", 
            76: "Woodblock Hi", 
            77: "Woodblock Low", 
            80: "Triangle Mute",
            81: "Triangle Open",
            87: "Shit does not exist this high."
            }'''

bad_note = [75, 64, 54, 61, 62, 63, 65, 58, 66, 60, 56, 76, 77, 80, 81, 87, 67, 68]


for root, dirs, files in os.walk(path):
    for file in files:
        fullpath = os.path.join(root, file)
        if file.endswith(".mid"):
            file_count += 1
            changed = False
            found_bad_note = False
            pattern = midi.read_midifile(fullpath)
            for track in pattern:
                for events in track:
                    if events.name == "Note On":
                        note = events.get_pitch()
                        if note in bad_note:
                            found_bad_note = True
            
            if found_bad_note:
                os.remove(fullpath)
                deleted_notes += 1
                #print(fullpath)


print "Done."
print "%d files were deleted out of %d files total." % (deleted_notes, file_count)