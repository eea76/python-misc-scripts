import os

my_dir = input("Enter a directory: ")
extension = input("Enter file extension: ")
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
            #os.rename(fullpath, file_dir + "/JA" + name[3:])
            #print(file_dir + "/ELC " + name[3:])
            changed += 1
            print(fullpath)

rename(my_dir)

print("Changed %s files" % changed)