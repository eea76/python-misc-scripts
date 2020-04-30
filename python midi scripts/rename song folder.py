import os
path = raw_input("Enter the path: ")
count = 0

final_list = []

for root, dirs, files in os.walk(path):
    for file in files:
        fullpath = os.path.join(root, file)
        if file.endswith(".mid"):
            if os.path.dirname(fullpath).endswith("songs") or os.path.dirname(fullpath).endswith("song"):
                old = os.path.dirname(fullpath)
                if old.endswith("song"):
                    new = old.replace('song', 'full song')
                    
                elif old.endswith("songs"):
                    new = old.replace('songs', 'full song')
                    
                os.rename(old, new)

                count += 1

          


print "%s files found." % count