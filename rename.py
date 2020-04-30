import os
path = '/Users/elon.arbiture/Desktop/to natasha⁩/'
files = os.listdir(path)
i = 1

for file in files:
    #this replaces occurences of the word 'large' with 'thumbnail'
    if 'txt.csv' in file:
      new_file = file.replace('txt.csv', 'csv')

    #this renames the file
    os.rename(os.path.join(path, file), os.path.join(path, new_file))
    i = i+1
    print file
