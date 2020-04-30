import os

source = raw_input("Please enter source path: ")
empty_folders = 0
empty_dir_list = []

def empty_dir(source):
    global empty_folders, empty_dir_list
    files = os.listdir(source)
    for f in files:
        sourcepath = ("%s/%s" % (source, f))
        if os.path.isdir(sourcepath):
            if not os.listdir(sourcepath):
                print sourcepath + " is empty"
                empty_folders += 1
                empty_dir_list.append(sourcepath)

            empty_dir(sourcepath)

def delete_empty_dir():
    for folder in empty_dir_list:
        os.rmdir(folder)

empty_dir(source)
print

if empty_folders > 0:
    print "Found %s empty dirs." % empty_folders
    to_delete = raw_input("Do you want to delete them? y/n ")
    if to_delete.lower() == "y":
        delete_empty_dir()
        print "%s empty directories have been deleted." % empty_folders
    else:
        print "\nThey have not been deleted."
else:
    print "No empty directories were found."