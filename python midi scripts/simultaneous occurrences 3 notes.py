# This script finds midi files where any given three notes
# occur in the same file but not necessarily at the SAME TIME

import midi, os, sys
from midi import *

path = "/Users/elon/Desktop/python midi scripts/toms transform"
file_count = 0
found_count = 0
found_list = []


first_note = int(raw_input("Enter the first note: "))
second_note = int(raw_input("Enter the second note: "))
third_note = int(raw_input("Enter the third note: "))

dest_list = [first_note, second_note]
#dupes = open("transform count.txt", "a")
first_note_list = []
second_note_list = []
third_note_list = []

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
                        elif note == third_note:
                            third_note_list.append(fullpath)

print len(set(first_note_list))
print len(set(second_note_list))
print len(set(third_note_list))

matches1 = set(first_note_list) & set(second_note_list) 

matches = matches1 & set(third_note_list)

my_list = list(matches)
my_list.sort()

for x in my_list:
    print x
print len(my_list)