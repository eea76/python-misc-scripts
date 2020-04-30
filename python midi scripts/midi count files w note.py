import midi, os, sys
from midi import *

path = "/Users/elon/Desktop/python midi scripts/7midi grooves GM transform 49 to 54"
file_count = 0
found_count = 0
found_list = []
#my_note = raw_input("Enter the note you wish to look for: ")
'''my_dict = {
            39: "Hand Clap",
            75: "Claves",
            45: "Floor Tom High", 
            64: "Conga Low", 
            44: "Hi Hat Pedal", 
            54: "Tambourine", 
            50: "Rack Tom Low Mid", 
            61: "Bongo Low", 
            62: "Conga Hi Mute", 
            63: "Conga Hi Open", 
            65: "Timbale Hi", 
            50: "Rack Tom Hi Mid", 
            45: "Rack Tom Hi", 
            60: "Bongo Hi", 
            66: "Timbale Low", 
            49: "Cymbal Crash 1",
            58: "Vibraslap (lol)", 
            52: "Cymbal Chinese", 
            55: "Cymbal Splash", 
            57: "Cymbal Crash 2", 
            50: "Ride Bell", 
            56: "Cowbell", 
            67: "Agogo Hi", 
            68: "Agogo Low", 
            76: "Woodblock Hi", 
            77: "Woodblock Low", 
            80: "Triangle Mute",
            81: "Triangle Open",
            87: "Shit does not exist this high",
            53: "Ride Bell",
            59: "Cymbal Ride 2",
            48: "Rack Tom: Hi Mid",
            47: "Rack Tom: Low Mid",
            43: "Floor Tom Hi",
            }'''

my_dict = {
    49 : "asld;fkjasld;fj",
    54: "fajfja"
}


#dupes = open("transform count.txt", "a")
for midi_note, instrument in my_dict.items(): 
    found_count = 0
    found_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            fullpath = os.path.join(root, file)
            if file.endswith(".mid"):
                file_count += 1
                found = False
                pattern = midi.read_midifile(fullpath)
                for track in pattern:
                    for events in track:
                        if events.name == "Note On":
                            note = events.get_pitch()
                            if note == midi_note:
                                found = True

                    if found:
                        found_count += 1
                        found_list.append(fullpath)

        #if found_count > 1:
        #    print "Note %s, %s: %s files." % (notes, dest_list, found_count)
        #dupes.write("Note %s: %s files.\n" % (notes, found_count))

    print "Note %s (%s): %s files" % (midi_note, instrument, found_count)
    


    #for x in found_list:
        #print x

print "Done."
#print found_list
#print "%d matching files were found out of %d files total." % (found_count, file_count)
