# USE THIS SCRIPT TO ADD THE GENRE ABBREVIATION TO EACH MIDI FILE
# IN THAT GENRE (have to manually change it in line 19)   

import os, sys


my_dir = input("Enter a directory: ")
extension = input("Enter file extension: ")
abbreviation = "/" + input("Enter the abbrevation with a space afterwards I think: ")
changed = 0

def rename(directory):
    global changed
    files = os.listdir(directory)
    for name in files:
        fullpath = ("%s/%s" % (directory, name))
        if os.path.isdir(fullpath):
            rename(fullpath)
        elif name.endswith(extension):
            file_dir = os.path.dirname(fullpath)
            os.rename(fullpath, file_dir + abbreviation + name)
            #print(file_dir + "/ELC " + name[3:])
            changed += 1
            #print(fullpath)

rename(my_dir)

print("Changed %s files" % changed)