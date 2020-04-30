
import os, sys, shutil
from decimal import Decimal

path = input("Enter a path: ")

for library in os.listdir(path):
  for root, dirs, files in os.walk(path+library):
    for file in files:
      sizePath = os.path.join(root,file)
      size = Decimal(Decimal(os.path.getsize(sizePath))/(1024*1024))#see below
      if (size >= 100):
       	print(file)
       	print(round(size,1))

  #divide by 1024 to see in kilobytes
  #divide by 1048576 to see in megabytes
