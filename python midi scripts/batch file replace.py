# USE THIS SCRIPT TO REPLACE THE FOLLOWING IN FILENAMES:

#Clave > Stick
#Conga > Tom
#Cowbell > Ride


import os, sys

path = "/Users/elon/Desktop/python midi scripts/midi grooves w name replace"
count = 0
filelength = 0
old_name = input("Enter the OLD name you want to replace: ")
new_name = input("Enter the NEW name you want to replace it with: ")
for root, dirs, files in os.walk(path):
    for name in files:
        if old_name in name:
            #print(files)
            fullpath = root + "/" + name
            #print(fullpath)
            count+=1
            os.rename(fullpath, root + "/" + name.replace(old_name, new_name))  
        
print("%s files renamed!" % count)
