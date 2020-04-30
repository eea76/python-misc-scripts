# This script looks at midi files in a directory and
# adds the time signature to the filename

import midi, os
from midi import *

mididb = open("mididb.txt", "a")

path = raw_input("Enter the path name: ")
found_count = 0
file_count = 0
changed_count = 0
p_id = 1

mtype_dict = {"Bridge": 1, "Pre-Chorus" : 2 , "Chorus" : 3, "Intro" : 4, "Verse" : 5, "Outro" : 6,
              "Fill" : 7, "Hybrid" : 8, "Full Song": 9}

subgenre_dict = {"Crack" : 1, "Funk" : 2, "Waltz" : 3, "Mambo" : 4, "Ballad" : 5, "Cajun" : 6, "Zydeco" : 6, 
                "Secondline" : 7, "Jump" : 8, "Streetbeat" : 9, "12-Bar" : 10, "Rock" : 11, "Train" : 12,
                "Tribal" : 13, "Surf" : 14, "Blues" : 15, "Fusion" : 16, "Be Bop" : 17, "Soca" : 18, "Neo-Disco" : 19,
                "Paradiddle" : 20, "Afro Pop":  21, "African": 22, "Fanga" : 23, "Candombe" : 24, "Calypso" : 25, 
                "Highlife" : 26, "Samba" : 27, "Progressive" : 28, "Alternative" : 29}


genre_dict = {"BE" : 1, "BB" : 2, "CTY" : 3, "HR" : 4,
              "JA" : 5, "PNK" : 6, "RNB" : 7, "RCK" : 8, "WLD" : 9,
              "PRG" : 8}


style_dict = {"Basic" : 1, "Swing" : 2, "Shuffle" : 3, "Straight" : 4, "Triplets" : 5, "2-Feel" : 6, 
              "4-Feel" : 7, "8ths Feel" : 8, "16ths Feel" : 9, "Half-Time Feel" : 10, "HFT" : 10,
              "Half-Time" : 11, "HT" : 11, "Quarter Notes" : 12, "QTR" : 12, "Four on the Floor" : 13, 
              "42TF" : 13, "Push" : 14, "Heartbeat" : 15, "Displaced" : 16, "Busy" : 17, "Upbeat" : 18,
              "Clave" : 19, "Linear" : 20, "Off Beat" : 21, "Loud Jazz" : 22, "Soft Jazz" : 23, "Slow Jazz" : 24,
              "Double-Time" : 25, "2x" : 25, "Backbeat" : 26, "Flow" : 27, "Moderate" : 28, "Driving" : 29,
              "Mixed" : 30, "Combos" : 31}

time_dict = {"3/4" : 1, "4/4" : 2, "5/4" : 3, "6/4" : 4, "7/4" : 5, "5/8" : 6,
             "6/8" : 7, "7/8" : 8, "9/8" : 9, "12/8" : 10}

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
                    if events.name == "Time Signature":
                        top = events.get_numerator()

                        bottom = events.get_denominator()
                        ts = str(top) + "/" + str(bottom)


            splitfile = file.split(" ")
            filename = " ".join(splitfile[3:])[:-4]
            splitrelpath = os.path.dirname(fullpath).split("/")
            relpath = "/".join(splitrelpath[7:])

            mtypedb = 0
            for key, value in mtype_dict.items():
                if key in file:
                    mtypedb = value


            subgenredb = 0     
            for key, value in subgenre_dict.items():
                if key in file:
                    subgenredb = value


            genredb = 0
            for key, value in genre_dict.items():
                if key in file:
                    genredb = value


            styledb = 0
            for key, value in style_dict.items():
                if key in file:
                    styledb = value

            timedb = 0
            for key, value in time_dict.items():
                if key == ts:
                    timedb = value


            #print "%s,%s,%s,%s,%s,%s,%s,%s" % (p_id, filename, genredb, subgenredb, styledb, mtypedb, timedb, relpath)
            mididb.write("%s,%s,%s,%s,%s,%s,%s,%s\n" % (p_id, filename, genredb, subgenredb, styledb, mtypedb, timedb, relpath))
            p_id+=1
mididb.close()

print "Done."
print found_count
print "%d files were changed out of %d files total." % (changed_count, file_count)