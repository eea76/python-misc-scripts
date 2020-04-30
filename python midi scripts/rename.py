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
            if '  ' in name:
                new_name = name.replace('  ', ' ')
                print("OLD: ", name)
                print("NEW: ", new_name)

                print("OLD FULLPATH: ", fullpath)
                print("NEW FULLPATH: ", os.path.dirname(fullpath) + "/" + new_name)
                print()
                file_dir = os.path.dirname(fullpath)
                os.rename(fullpath, file_dir + "/" + new_name)
                changed += 1


rename(my_dir)

print("Changed %s files" % changed)