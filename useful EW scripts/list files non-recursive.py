'''
This program lists the contents (files and folders) of a single
specified directory (non-recursive)and includes the option to
export the list to a  .txt file if desired!
'''

# This only looks at a single directory and 
# returns a matching filetype in that directory.

import os

path = input("Enter a filepath: ")
extension = input("Enter a file extension: ")

txtfile_name = input("Enter a file name (blank to skip): ")

if txtfile_name == "":
    txtfile_name = txtfile_name
else:
    if not txtfile_name.endswith(".txt"):
        txtfile_name = txtfile_name + ".txt"
    else:
        pass


filelist = os.listdir(path)

#-----------
# Do not fuck with above code. Change conditions here as needed:

found = 0
    
for file in filelist:
    if txtfile_name != "":
        txtfile = open("/Users/elon/Desktop/" + txtfile_name, "a")
        if file.endswith(extension):
            found += 1
            txtfile.write(file + "\n")

    else:
        if file.endswith(extension):
            found += 1
            print(file)
        else:
            pass
            
if txtfile_name != "":
    txtfile.close()
print("\n%d %s files found." % (found, extension))