import os, sys, shutil

path = input("Enter a path: ")
extension = input("Enter a file extension: ")
total = 0

for library in os.listdir(path):

    if not ("." in library):
        #print(library)
        counter = 0
        for root, dirs, files in os.walk(path + library):
            for file in files:
               #print(file)
               if file.endswith(extension):
                  counter += 1
                  total += 1	
        print("%s: %d" % (library, counter))    


print("\nTotal: %d files" % total)
#print(printstring)
