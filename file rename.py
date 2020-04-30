import os, sys

path = input("enter the folder path: ")
count = 0
filelength = 0
for root, dirs, files in os.walk(path):
    for name in files:
        if ".JPG" in name:
            fullpath = root + "/" + name
            print(fullpath)
            print(name)
            count+=1

            # use following rename statement accordingly:
            # or just write a better fucking script but fuck that
            # os.rename(fullpath, root + "/" + name.replace(name, count+".JPG", 1))


print("%s files renamed!" % count)
