import os, sys

path = "/Users/elonarbiture/eea/My Media/Music/Mp3s/Archived/"
count = 0
filelength = 0
for root, dirs, files in os.walk(path):
    for name in files:
        if name.endswith(".mp3"):
            fullpath = root + "/" + name
            print(fullpath)
            print(name)
            count+=1

            # use following rename statement accordingly:
            #os.rename(fullpath, root + "/" + name.replace(" - ", " ", 1))
        
    
print("%s files renamed!" % count)
