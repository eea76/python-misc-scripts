import midi, os
from midi import *

GM_Dict = {
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
                }


path = "/Users/elon/Desktop/midi grooves GM"
file_count = 0
changed_count = 0
note_43_list = []
note_64_list = []
note_39_list = []
note_75_list = []
note_44_list = []
note_54_list = []
note_47_list = []
note_61_list = []
note_62_list = []
note_63_list = []
note_65_list = []
note_48_list = []
note_50_list = []
note_60_list = []
note_66_list = []
note_49_list = []
note_58_list = []
note_52_list = []
note_55_list = []
note_57_list = []
note_53_list = []
note_56_list = []
note_67_list = []
note_68_list = []
note_76_list = []
note_77_list = []
note_80_list = []
note_81_list = []
note_87_list = []
note_59_list = []


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
                        if note == 43:
                            note_43_list.append(fullpath)
                        elif note == 39:
                            note_39_list.append(fullpath)
                        elif note == 75:
                            note_75_list.append(fullpath)
                        elif note == 44:
                            note_44_list.append(fullpath)
                        elif note == 54:
                            note_54_list.append(fullpath)
                        elif note == 47:
                            note_47_list.append(fullpath)
                        elif note == 61:
                            note_61_list.append(fullpath)
                        elif note == 62:
                            note_62_list.append(fullpath)
                        elif note == 64:
                            note_64_list.append(fullpath)
                        elif note == 63:
                            note_63_list.append(fullpath)
                        elif note == 65:
                            note_65_list.append(fullpath)
                        elif note == 48:
                            note_48_list.append(fullpath)
                        elif note == 50:
                            note_50_list.append(fullpath)
                        elif note == 60:
                            note_60_list.append(fullpath)
                        elif note == 66:
                            note_66_list.append(fullpath)
                        elif note == 49:
                            note_49_list.append(fullpath)
                        elif note == 58:
                            note_58_list.append(fullpath)
                        elif note == 52:
                            note_52_list.append(fullpath)
                        elif note == 55:
                            note_55_list.append(fullpath)
                        elif note == 57:
                            note_57_list.append(fullpath)
                        elif note == 53:
                            note_53_list.append(fullpath) 
                        elif note == 56:
                            note_56_list.append(fullpath)
                        elif note == 67:
                            note_67_list.append(fullpath)
                        elif note == 68:
                            note_68_list.append(fullpath)
                        elif note == 76:
                            note_76_list.append(fullpath)
                        elif note == 77:
                            note_77_list.append(fullpath)
                        elif note == 80:
                            note_80_list.append(fullpath)
                        elif note == 81:
                            note_81_list.append(fullpath)
                        elif note == 87:
                            note_87_list.append(fullpath)
                        elif note == 59:
                            note_59_list.append(fullpath)

            
                        
            if changed:
                midi.write_midifile(fullpath, pattern)
                changed_count += 1

# Fucking insane operations below:
last_list = []

all_note37_lists = [
            set(note_39_list),
            set(note_75_list)]

final_note37_list = []

for x in all_note37_lists[0]:
    if x in all_note37_lists[1]:
        final_note37_list.append(x)
for x in all_note37_lists[1]:
    if x in all_note37_lists[0]:
        final_note37_list.append(x)

#print len(final_note37_list)
#print len(set(final_note37_list))
for x in set(final_note37_list):
    last_list.append(x)
print

#____________________#

all_note41_lists = [
            set(note_43_list),
            set(note_64_list)]

final_note41_list = []

for x in all_note41_lists[0]:
    if x in all_note41_lists[1]:
        final_note41_list.append(x)
for x in all_note41_lists[1]:
    if x in all_note41_lists[0]:
        final_note41_list.append(x)

#print len(final_note41_list)
#print len(set(final_note41_list))
for x in set(final_note41_list):
    last_list.append(x)
print

#____________________#

all_note34_lists = [
            set(note_44_list),
            set(note_54_list)]

final_note34_list = []

for x in all_note34_lists[0]:
    if x in all_note34_lists[1]:
        final_note34_list.append(x)
for x in all_note34_lists[1]:
    if x in all_note34_lists[0]:
        final_note34_list.append(x)

#print len(final_note34_list)
#print len(set(final_note34_list))
for x in set(final_note34_list):
    last_list.append(x)
print

#____________________#

all_note43_lists = [
            set(note_47_list), 
            set(note_61_list), 
            set(note_62_list), 
            set(note_63_list), 
            set(note_65_list)]

final_note43_list = []

for x in all_note43_lists[0]:
    if x in all_note43_lists[1]:
        final_note43_list.append(x)
    if x in all_note43_lists[2]:
        final_note43_list.append(x)
    if x in all_note43_lists[3]:
        final_note43_list.append(x)
    if x in all_note43_lists[4]:
        final_note43_list.append(x)

for x in all_note43_lists[1]:
    if x in all_note43_lists[0]:
        final_note43_list.append(x)
    if x in all_note43_lists[2]:
        final_note43_list.append(x)
    if x in all_note43_lists[3]:
        final_note43_list.append(x)
    if x in all_note43_lists[4]:
        final_note43_list.append(x)

for x in all_note43_lists[2]:
    if x in all_note43_lists[0]:
        final_note43_list.append(x)
    if x in all_note43_lists[1]:
        final_note43_list.append(x)
    if x in all_note43_lists[3]:
        final_note43_list.append(x)
    if x in all_note43_lists[4]:
        final_note43_list.append(x)

for x in all_note43_lists[3]:
    if x in all_note43_lists[0]:
        final_note43_list.append(x)
    if x in all_note43_lists[1]:
        final_note43_list.append(x)
    if x in all_note43_lists[2]:
        final_note43_list.append(x)
    if x in all_note43_lists[4]:
        final_note43_list.append(x)

for x in all_note43_lists[4]:
    if x in all_note43_lists[0]:
        final_note43_list.append(x)
    if x in all_note43_lists[1]:
        final_note43_list.append(x)
    if x in all_note43_lists[2]:
        final_note43_list.append(x)
    if x in all_note43_lists[3]:
        final_note43_list.append(x)

#print len(final_note43_list)
#print len(set(final_note43_list))
for x in set(final_note43_list):
    last_list.append(x)
print

#____________________#

all_note45_lists = [
            set(note_48_list),
            set(note_50_list),
            set(note_60_list),
            set(note_66_list)]

final_note45_list = []

for x in all_note45_lists[0]:
    if x in all_note45_lists[1]:
        final_note45_list.append(x)
    if x in all_note45_lists[2]:
        final_note45_list.append(x)
    if x in all_note45_lists[3]:
        final_note45_list.append(x)

for x in all_note45_lists[1]:
    if x in all_note45_lists[0]:
        final_note45_list.append(x)
    if x in all_note45_lists[2]:
        final_note45_list.append(x)
    if x in all_note45_lists[3]:
        final_note45_list.append(x)

for x in all_note45_lists[2]:
    if x in all_note45_lists[0]:
        final_note45_list.append(x)
    if x in all_note45_lists[1]:
        final_note45_list.append(x)
    if x in all_note45_lists[3]:
        final_note45_list.append(x)

for x in all_note45_lists[3]:
    if x in all_note45_lists[0]:
        final_note45_list.append(x)
    if x in all_note45_lists[1]:
        final_note45_list.append(x)
    if x in all_note45_lists[2]:
        final_note45_list.append(x)

#print len(final_note45_list)
#print len(set(final_note45_list))
for x in set(final_note45_list):
    last_list.append(x)
print

#____________________#

all_note54_lists = [
            set(note_49_list),
            set(note_58_list)]

final_note54_list = []

for x in all_note54_lists[0]:
    if x in all_note54_lists[1]:
        final_note54_list.append(x)
for x in all_note54_lists[1]:
    if x in all_note54_lists[0]:
        final_note54_list.append(x)

#print len(final_note54_list)
#print len(set(final_note54_list))
for x in set(final_note54_list):
    last_list.append(x)
print

#____________________#

all_note56_lists = [
            set(note_52_list),
            set(note_55_list),
            set(note_57_list)]

final_note56_list = []

for x in all_note56_lists[0]:
    if x in all_note56_lists[1]:
        final_note56_list.append(x)
    if x in all_note56_lists[2]:
        final_note56_list.append(x)

for x in all_note56_lists[1]:
    if x in all_note56_lists[0]:
        final_note56_list.append(x)
    if x in all_note56_lists[2]:
        final_note56_list.append(x)

for x in all_note56_lists[2]:
    if x in all_note56_lists[0]:
        final_note56_list.append(x)
    if x in all_note56_lists[1]:
        final_note56_list.append(x)

#print len(final_note56_list)
#print len(set(final_note56_list))
for x in set(final_note56_list):
    last_list.append(x)
print

#____________________#

all_note51_lists = [
            set(note_53_list), 
            set(note_56_list), 
            set(note_67_list), 
            set(note_68_list), 
            set(note_76_list),
            set(note_77_list),
            set(note_80_list),
            set(note_81_list),
            set(note_87_list)]

final_note51_list = []

for x in all_note51_lists[0]:
    if x in all_note51_lists[1]:
        final_note51_list.append(x)
    if x in all_note51_lists[2]:
        final_note51_list.append(x)
    if x in all_note51_lists[3]:
        final_note51_list.append(x)
    if x in all_note51_lists[4]:
        final_note51_list.append(x)
    if x in all_note51_lists[5]:
        final_note51_list.append(x)
    if x in all_note51_lists[6]:
        final_note51_list.append(x)
    if x in all_note51_lists[7]:
        final_note51_list.append(x)
    if x in all_note51_lists[8]:
        final_note51_list.append(x)

for x in all_note51_lists[1]:
    if x in all_note51_lists[0]:
        final_note51_list.append(x)
    if x in all_note51_lists[2]:
        final_note51_list.append(x)
    if x in all_note51_lists[3]:
        final_note51_list.append(x)
    if x in all_note51_lists[4]:
        final_note51_list.append(x)
    if x in all_note51_lists[5]:
        final_note51_list.append(x)
    if x in all_note51_lists[6]:
        final_note51_list.append(x)
    if x in all_note51_lists[7]:
        final_note51_list.append(x)
    if x in all_note51_lists[8]:
        final_note51_list.append(x)

for x in all_note51_lists[2]:
    if x in all_note51_lists[0]:
        final_note51_list.append(x)
    if x in all_note51_lists[1]:
        final_note51_list.append(x)
    if x in all_note51_lists[3]:
        final_note51_list.append(x)
    if x in all_note51_lists[4]:
        final_note51_list.append(x)
    if x in all_note51_lists[5]:
        final_note51_list.append(x)
    if x in all_note51_lists[6]:
        final_note51_list.append(x)
    if x in all_note51_lists[7]:
        final_note51_list.append(x)
    if x in all_note51_lists[8]:
        final_note51_list.append(x)

for x in all_note51_lists[3]:
    if x in all_note51_lists[0]:
        final_note51_list.append(x)
    if x in all_note51_lists[1]:
        final_note51_list.append(x)
    if x in all_note51_lists[2]:
        final_note51_list.append(x)
    if x in all_note51_lists[4]:
        final_note51_list.append(x)
    if x in all_note51_lists[5]:
        final_note51_list.append(x)
    if x in all_note51_lists[6]:
        final_note51_list.append(x)
    if x in all_note51_lists[7]:
        final_note51_list.append(x)
    if x in all_note51_lists[8]:
        final_note51_list.append(x)

for x in all_note51_lists[4]:
    if x in all_note51_lists[0]:
        final_note51_list.append(x)
    if x in all_note51_lists[1]:
        final_note51_list.append(x)
    if x in all_note51_lists[2]:
        final_note51_list.append(x)
    if x in all_note51_lists[3]:
        final_note51_list.append(x)
    if x in all_note51_lists[5]:
        final_note51_list.append(x)
    if x in all_note51_lists[6]:
        final_note51_list.append(x)
    if x in all_note51_lists[7]:
        final_note51_list.append(x)
    if x in all_note51_lists[8]:
        final_note51_list.append(x)

for x in all_note51_lists[5]:
    if x in all_note51_lists[0]:
        final_note51_list.append(x)
    if x in all_note51_lists[1]:
        final_note51_list.append(x)
    if x in all_note51_lists[2]:
        final_note51_list.append(x)
    if x in all_note51_lists[3]:
        final_note51_list.append(x)
    if x in all_note51_lists[4]:
        final_note51_list.append(x)
    if x in all_note51_lists[6]:
        final_note51_list.append(x)
    if x in all_note51_lists[7]:
        final_note51_list.append(x)
    if x in all_note51_lists[8]:
        final_note51_list.append(x)

for x in all_note51_lists[6]:
    if x in all_note51_lists[0]:
        final_note51_list.append(x)
    if x in all_note51_lists[1]:
        final_note51_list.append(x)
    if x in all_note51_lists[2]:
        final_note51_list.append(x)
    if x in all_note51_lists[3]:
        final_note51_list.append(x)
    if x in all_note51_lists[4]:
        final_note51_list.append(x)
    if x in all_note51_lists[5]:
        final_note51_list.append(x)
    if x in all_note51_lists[7]:
        final_note51_list.append(x)
    if x in all_note51_lists[8]:
        final_note51_list.append(x)

for x in all_note51_lists[7]:
    if x in all_note51_lists[0]:
        final_note51_list.append(x)
    if x in all_note51_lists[1]:
        final_note51_list.append(x)
    if x in all_note51_lists[2]:
        final_note51_list.append(x)
    if x in all_note51_lists[3]:
        final_note51_list.append(x)
    if x in all_note51_lists[4]:
        final_note51_list.append(x)
    if x in all_note51_lists[5]:
        final_note51_list.append(x)
    if x in all_note51_lists[6]:
        final_note51_list.append(x)
    if x in all_note51_lists[8]:
        final_note51_list.append(x)

for x in all_note51_lists[8]:
    if x in all_note51_lists[0]:
        final_note51_list.append(x)
    if x in all_note51_lists[1]:
        final_note51_list.append(x)
    if x in all_note51_lists[2]:
        final_note51_list.append(x)
    if x in all_note51_lists[3]:
        final_note51_list.append(x)
    if x in all_note51_lists[4]:
        final_note51_list.append(x)
    if x in all_note51_lists[5]:
        final_note51_list.append(x)
    if x in all_note51_lists[6]:
        final_note51_list.append(x)
    if x in all_note51_lists[7]:
        final_note51_list.append(x)

#print len(final_note51_list)
#print len(set(final_note51_list))
for x in set(final_note51_list):
    last_list.append(x)
print
last_list.sort()
for x in last_list:
    print x[50:]
print len(last_list)
print "Done."
print "%d files were changed out of %d files total." % (changed_count, file_count)