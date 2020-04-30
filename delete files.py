import os, sys

path = input("enter the folder path: ")
filename = input('enter filename: ')
count = 0
filelength = 0
for root, dirs, files in os.walk(path):
    for name in files:
        if filename in name:
            fullpath = root + "/" + name
            print(fullpath)
            print(name)
            count+=1

            # use following rename statement accordingly:
            # os.rename(fullpath, root + "/" + name.replace(" ", "-", 1))
            os.remove(fullpath)
        
    
print("%s files DELETED FOREVER" % count)
