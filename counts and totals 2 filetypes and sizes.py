import os, sys, shutil

if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = input("Enter the full path to Libraries: ")
txtfile = open(r"C:\Users\JK X64\Desktop\Dan Brown Windows Drive.txt", "w", encoding ="utf-8")
ewiTotal = 0
ewsTotal = 0
totalsize = 0

def outputtotal(text):
    print(text)
    txtfile.write(text + "\n")
    

# This script looks at each library and counts the number of .ews files in each
# and then prints the total .ews files at the end

#defining library as the last folder in the path name

for library in os.listdir(path):
    if not os.path.isdir(path + library): continue # <-- saying if the filename is not a directory, SKIP that iteration
    sys.stdout.write(library + ": ")
    txtfile.write(library + ": ")
    #print(library) - print automatically inserts a return
    #sys.stdout.write - does no formatting; takes a string and prints
    ewiCounter = 0
    ewsCounter = 0
    librarysize = 0
    for root, dirs, files in os.walk(path + library):
       os.chdir(root) # sets the current iterated directory; all relatives are relative to this path
       for file in files:    
           if file.endswith('.ewi'):
              ewiCounter += 1
              ewiTotal += 1
              librarysize += os.path.getsize(file)
           elif file.endswith('.ews'):
              ewsCounter += 1
              ewsTotal += 1
              librarysize += os.path.getsize(file)
    totalsize += librarysize
    outputtotal("%d .ewi, %d .ews" % (ewiCounter, ewsCounter)) 
    
outputtotal("\nTotal: %d .ewi, %d .ews" % (ewiTotal, ewsTotal)) 
outputtotal("Total: %d files, %d bytes" % (ewiTotal + ewsTotal, totalsize))

txtfile.close()

# the comma separates parameters to the function, outputs with tabs in between
# \n = new line; just like hitting enter, works even inside a string
# ('\' is a special character in python


