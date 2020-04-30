# os.path.getsize(path filename)

import os
directory = input("Enter the directory: ")
minsize = input("Enter the minimum /file size (in MB) you want to return: ")
minsize = int(minsize) * 1024 * 1024
filesfound = []
for root, dirs, files in os.walk(directory):
    for filename in files:
        fullpath = root + "/" + filename
        try:
            filesize = os.path.getsize(fullpath)
            if filesize >= minsize:
                filesfound.append({"Path" : fullpath, "Size" : filesize})
        except KeyboardInterrupt:
            raise
        except:
            pass

# [ { "path":"abc", "size":123 } ,
#   { "path":"def", "size":456 } ]

def itemkey(x):
    return x["Size"]

filesfound.sort(key=itemkey, reverse=True)


for file in filesfound:
    print("%d\t%s" % (file["Size"], file["Path"]))
