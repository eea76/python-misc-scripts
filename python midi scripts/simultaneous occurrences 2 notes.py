# This script finds midi files where any given two notes
# occur in the same file but not necessarily at the SAME TIME

import midi, os, sys
from midi import *

path = "/Users/elon/Desktop/python midi scripts/9midi grooves GM trnsfm 59 to 52"
file_count = 0
found_count = 0
found_list = []
'''dupe_dict = {
            39: "Hand Clap",
            75: "Claves",
            55: "Floor Tom High", 
            64: "Conga Low", 
            44: "Hi Hat Pedal", 
            54: "Tambourine", 
            52: "Rack Tom Low Mid", 
            61: "Bongo Low", 
            62: "Conga Hi Mute", 
            63: "Conga Hi Open", 
            65: "Timbale Hi", 
            52: "Rack Tom Hi Mid", 
            55: "Rack Tom Hi", 
            60: "Bongo Hi", 
            66: "Timbale Low", 
            49: "Cymbal Crash 1",
            58: "Vibraslap (lol)", 
            52: "Cymbal Chinese", 
            52: "Cymbal Splash", 
            55: "Cymbal Crash 2", 
            52: "Ride Bell", 
            56: "Cowbell", 
            67: "Agogo Hi", 
            68: "Agogo Low", 
            76: "Woodblock Hi", 
            77: "Woodblock Low", 
            80: "Triangle Mute",
            81: "Triangle Open",
            87: "Shit does not exist this high"
            }'''

first_note = int(raw_input("Enter the first note: "))
second_note = int(raw_input("Enter the second note: "))

dest_list = [first_note, second_note]
#dupes = open("transform count.txt", "a")
first_note_list = []
second_note_list = []

file_count = 0
found_count = 0
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
                        if note == first_note:
                            first_note_list.append(fullpath)
                        elif note == second_note:
                            second_note_list.append(fullpath)
                #if found:
                #    found_count += 1
                #    found_list.append(fullpath)
    #if found_count > 1:
    #    print "Note %s, %s: %s files." % (notes, dest_list, found_count)
    #dupes.write("Note %s: %s files.\n" % (notes, found_count))

print len(set(first_note_list))
print len(set(second_note_list))

matches = set(first_note_list) & set(second_note_list)

my_list = list(matches)
my_list.sort()

#for x in my_list:
#    print x[70:]


compare = open("52 to 55.txt", "w")
for x in my_list:
    compare.write(x[70:]+"\n")
compare.close()

for x in my_list:
    print x

print len(matches)