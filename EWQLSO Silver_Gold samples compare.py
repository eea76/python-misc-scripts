import os, sys, shutil

def walkdir(path):
    files = os.listdir(path)
    for f in files:
        fullpath = ("%s\\%s" % (path, f))
        print(fullpath)
        if os.path.isdir(fullpath):
            walkdir(fullpath)
            
lineNo = 0
destfile = open(r"/Users/michaelault/Desktop/Duplicate EWQLSO.txt", "w", encoding="utf-8")
def comparedir(source, destination, basepath = None):
    global destfile, lineNo
    if basepath is None:
        basepath = destination
    if not os.path.isdir(destination):
        lineNo = lineNo + 1
        destfile.write("%d: %s: not a folder\n" % (lineNo, destination.replace(basepath, "")))
        return
    files = os.listdir(source)
    for filename in files:
        sourcepath = ("%s/%s" % (source, filename))
        destinationpath = ("%s/%s" % (destination, filename))
        if os.path.isdir(sourcepath):
            comparedir(sourcepath, destinationpath, basepath)
        elif ".ews" in sourcepath:
            if os.path.isfile(destinationpath):
                lineNo = lineNo + 1
                destfile.write("%d: %s: file exists in both Silver and Gold Samples\n" % (lineNo, destinationpath.replace(basepath, "")))

comparedir(r"/Users/michaelault/Desktop/Libraries/EWQL Symphonic Orchestra Gold/Silver Samples/Silver Brass",
        r"/Users/michaelault/Desktop/Libraries/EWQL Symphonic Orchestra Gold/Gold Samples/Gold Brass")

comparedir(r"/Users/michaelault/Desktop/Libraries/EWQL Symphonic Orchestra Gold/Silver Samples/Silver Percussion",
        r"/Users/michaelault/Desktop/Libraries/EWQL Symphonic Orchestra Gold/Gold Samples/Gold Percussion")

comparedir(r"/Users/michaelault/Desktop/Libraries/EWQL Symphonic Orchestra Gold/Silver Samples/Silver Winds",
        r"/Users/michaelault/Desktop/Libraries/EWQL Symphonic Orchestra Gold/Gold Samples/Gold Winds")

comparedir(r"/Users/michaelault/Desktop/Libraries/EWQL Symphonic Orchestra Gold/Silver Samples/Silver Strings",
        r"/Users/michaelault/Desktop/Libraries/EWQL Symphonic Orchestra Gold/Gold Samples/Gold Strings")

destfile.close()
