import os, sys, shutil

def walkdir(path):
    files = os.listdir(path)
    for f in files:
        fullpath = ("%s\\%s" % (path, f))
        print(fullpath)
        if os.path.isdir(fullpath):
            walkdir(fullpath)
            
lineNo = 0
destfile = open(r"C:\Users\JK X64\Desktop\Mismatched Files Gold.txt", "w", encoding="utf-8")
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
        sourcepath = ("%s\\%s" % (source, filename))
        destinationpath = ("%s\\%s" % (destination, filename))
        destinationpath = destinationpath.replace(".wav", ".ews")
        if os.path.isdir(sourcepath):
            comparedir(sourcepath, destinationpath, basepath)
        elif ".wav" in sourcepath:
            if not os.path.isfile(destinationpath):
                lineNo = lineNo + 1
                destfile.write("%d: %s: file does not exist\n" % (lineNo, destinationpath.replace(basepath, "")))

comparedir(r"C:\Users\JK X64\Desktop\Gold Orchestra Raw and Encrypted\WAV Samples",
        r"C:\Users\JK X64\Desktop\Gold Orchestra Raw and Encrypted\Encrypted Samples\Gold Samples")

destfile.close()
