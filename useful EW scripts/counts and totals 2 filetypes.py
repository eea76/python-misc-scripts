# This script looks at each library and counts the number of 
# .ewi and .ews files in each and then prints 
# the total of each at the end
# can print to a .txt file if desired but shell output is sufficient usually

# try adding a "/" at the end of your path if it doesn't print anything

import os, sys, shutil

if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = input("Enter the full path to Libraries: ")
txtfilepath = input("Enter the full path of the output file (leave blank to skip): ")


ewiTotal = 0
ewsTotal = 0



#defining library as the last folder in the path name

for library in os.listdir(path):
    if not os.path.isdir(path + library): continue
    sys.stdout.write(library + ": ")
    if txtfilepath != "":
        txtfile = open(txtfilepath, "a", encoding ="utf-8")
        txtfile.write(library + ": ")
    #print(library) - print automatically inserts a return
    #sys.stdout.write - does no formatting; takes a string and prints
    ewiCounter = 0
    ewsCounter = 0
    for root, dirs, files in os.walk(path + library):
        for file in files:
           if file.endswith('.ewi'):
              ewiCounter += 1
              ewiTotal += 1    
           elif file.endswith('.ews'):
              ewsCounter += 1
              ewsTotal += 1   	
    print("%d .ewi, %d .ews" % (ewiCounter, ewsCounter)) 
    if txtfilepath != "":
        txtfile.write("%d .ewi, %d .ews\n" % (ewiCounter, ewsCounter))       

print("\nTotal: %d .ewi, %d .ews" % (ewiTotal, ewsTotal)) 


print("Total: ", ewiTotal + ewsTotal)

if txtfilepath != "":
    #txtfile = open(txtfilepath, "w", encoding ="utf-8")
    txtfile.write("\nTotal: %d .ewi, %d .ews\n" % (ewiTotal, ewsTotal))
    txtfile.write("Total: %d" % (ewiTotal + ewsTotal))
    txtfile.close()


