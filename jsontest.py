import csv
import json

csvfile = open('nocomma-test.csv', 'r')
jsonfile = open('stockists.json', 'w')

fieldnames = ('address1', 'address2', 'city', 'state', 'zip', 'lat', 'lng')
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')

jsonfile.close()
csvfile.close()