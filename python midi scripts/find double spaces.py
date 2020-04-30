import os
path = raw_input("Enter the path: ")
count = 0

final_list = []

for root, dirs, files in os.walk(path):
    for file in files:
        fullpath = os.path.join(root, file)
        if file.endswith(".mid"):
            if '  ' in file:
                print file
                count += 1
                new_fullpath = fullpath.replace('  ', ' ')
                print new_fullpath
                os.rename(fullpath, new_fullpath)
        
          


print "%s files found." % count