import os

# scans .ewc files in a directory and returns its associated product name.
# OS X
# should probably revise with .sep so it's cross-platform
# Regex is probably the way to do this better

path = "/Library/Application Support/East West/ProductChunks"

for file in os.listdir(path):
    if file.endswith(".ewc"):
        fullpath = path + "/" + file
        ewc = open(fullpath, "r", encoding = "utf-8")
        for line in ewc:
            line = line.strip()
            if line.startswith("T"):
                index = line.find('"')
                end_index = line.find('"', index + 1) # the second parameter in find() specifies at what index to start searching
                print("Chunk name: %s" % file)
                print("Product name: " + line[index + 1 : end_index])
                print()

