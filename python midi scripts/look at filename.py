import os
path = raw_input("Enter the path: ")
count = 0

final_list = []

for root, dirs, files in os.walk(path):
    for file in files:
        fullpath = os.path.join(root, file)
        if file.endswith(".mid"):

            styles = ["Basic", "Swing", "Shuffle", "Straight", "Triplets", "2-Feel",
              "4-Feel", "8ths Feel", "16ths Feel", "Half-Time Feel", "HFT", "Half-Time"
              "HT", "Quarter Notes", "QTR", "Four on the Floor", "42TF", "Push", "Heartbeat",
              "Displaced", "Busy", "Upbeat", "Clave", "Linear", "Off Beat", "Loud Jazz", "Soft Jazz",
              "Slow Jazz", "Double-Time", "2x", "Backbeat", "Flow", "Moderate", "Driving", "Mixed", "Combos"]

            for style in styles:
                if style in file:
                    styles.remove(style)
                    for style2 in styles:
                        if style2 in file:
                            print file
                            count += 1


print "%s files found." % count