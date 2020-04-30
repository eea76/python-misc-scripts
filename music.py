# This script looks at an exported iTunes playlist and returns its albums

import codecs

myfile = codecs.open('Music.txt', 'r', encoding='utf-16')
read_file = myfile.readlines()
album_list = [line.split('\t')[3] for line in read_file]
album_set = {x for x in album_list}

for x in sorted(album_set):
    print x