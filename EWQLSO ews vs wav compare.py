import os, sys, shutil

def walkdir(path):
    files = os.listdir(path)
    for f in files:
        fullpath = ("%s\\%s" % (path, f))
        print(fullpath)
        if os.path.isdir(fullpath):
            walkdir(fullpath)
            
lineNo = 0
destfile = open(r"/Users/michaelault/Desktop/Silver wav vs ews.txt", "w", encoding="utf-8")
def comparedir(source, destination, basepath = None):
    global destfile, lineNo
    if basepath is None:
        basepath = destination
    if not os.path.isdir(destination):
        lineNo = lineNo + 1
        destfile.write("%d: %s: not a folder\n" % (lineNo, destination)) #.replace(basepath, "")))
        return
    files = os.listdir(source)
    for filename in files:
        sourcepath = ("%s/%s" % (source, filename))
        destinationpath = ("%s/%s" % (destination, filename))
        destinationpath = destinationpath.replace(".ews", ".wav")
        if os.path.isdir(sourcepath):
            comparedir(sourcepath, destinationpath, basepath)
        else: #if ".ews" in sourcepath:
            if not os.path.isfile(destinationpath):
                lineNo = lineNo + 1
                destfile.write("%d: %s: file not found\n" % (lineNo, destinationpath.replace(basepath, "")))

comparedir(r"/Users/michaelault/Desktop/Libraries/EWQL Symphonic Orchestra Gold/Silver Samples/Silver Brass",
        r"/Users/michaelault/Desktop/Libraries/EWQL Symphonic Orchestra Gold/Reencrypt/Gold Brass")

comparedir(r"/Users/michaelault/Desktop/Libraries/EWQL Symphonic Orchestra Gold/Silver Samples/Silver Percussion",
        r"/Users/michaelault/Desktop/Libraries/EWQL Symphonic Orchestra Gold/Reencrypt/Gold Percussion")

comparedir(r"/Users/michaelault/Desktop/Libraries/EWQL Symphonic Orchestra Gold/Silver Samples/Silver Winds",
        r"/Users/michaelault/Desktop/Libraries/EWQL Symphonic Orchestra Gold/Reencrypt/Gold Winds")

comparedir(r"/Users/michaelault/Desktop/Libraries/EWQL Symphonic Orchestra Gold/Silver Samples/Silver Strings",
        r"/Users/michaelault/Desktop/Libraries/EWQL Symphonic Orchestra Gold/Reencrypt/Gold Strings")

destfile.close()
