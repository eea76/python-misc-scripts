# sort -n "filepath" - This terminal command sorts the lines of a file numerically, smallest to largest


import os

outfile = open(r"/Users/elon/Desktop/files.txt", 'w', encoding='utf-8')
basepath = "/Users/elon/"

for dirpath, dirnames, filenames in os.walk(basepath):
    for file in filenames:
        fullpath = os.path.join(dirpath, file)
        outfile.write("%d\t%s\n" % (os.path.getsize(fullpath), fullpath.replace(basepath, "")))

