#!/usr/bin/python
# This script will only remove trailing spaces from directory names. It is
# intended to be used specifically to fix naming problems with the Hollywood 
# Strings Library, and will not fix other file naming problems that can appear
# on windows, when accessing files created on a mac with incompatible naming.


import os
import re

exp = re.compile('.* $')

for root, dirs, files in os.walk(os.getcwd()):
    if not dirs == []:
        for folder in dirs:
            mat = re.match(exp, folder)
            if mat:
                stripfol = folder.strip()
                print("\noriginal: " + root + "/" + folder + "\nnew: " + root + "/" + stripfol)
                os.rename(os.path.join(root, folder), os.path.join(root, stripfol))
