# This script copies everything one from directory and pastes it
# to another directory.

# This script ignores .DS_Store files, .nov files, and duplicate files
# that already exist in the destination. 
# Good for verifying that two directories are identical.

import os, sys, shutil
import time, datetime


def walkdir(path):
    files = os.listdir(path)
    for f in files:
        fullpath = ("%s\\%s" % (path, f))
        #print(fullpath)
        if os.path.isdir(fullpath):
            walkdir(fullpath)

def get_source_size(source):
    global source_size
    global source_count
    files = os.listdir(source)
    for f in files:
        sourcepath = ("%s/%s" %(source,f))
        if os.path.isdir(sourcepath):
            get_source_size(sourcepath)
        elif f != ".DS_Store" and f[-4:] != ".nov":
            source_size += os.path.getsize(sourcepath)
            source_count += 1
            if source_count % 50000 == 0:
                print(source_count)
                print(f)
            #print(source_size)
            #print(sourcepath)
    return source_size

def get_destination_size(destination):
    global destination_size
    global destination_count
    files = os.listdir(destination)
    for f in files:
        destinationpath = ("%s/%s" %(destination,f))
        if os.path.isdir(destinationpath):
            get_destination_size(destinationpath)
        elif f != ".DS_Store" and f[-4:] != ".nov":
            destination_size += os.path.getsize(destinationpath)
            destination_count += 1
            if destination_count % 50000 == 0:
                print(destination_count)
                print(f)
    return destination_size


def copydir(source, destination):
    global copied
    global bytes_transferred
    global elapsed_time
    global my_source_size
    global my_destination_size
    global source_count
    global destination_count
    global next_output
    global copied_per_second_average
    global copied_per_second
    if not os.path.isdir(destination):
        os.mkdir(destination)
    files = os.listdir(source)

    for f in files:
        sourcepath = ("%s/%s" % (source, f))
        destinationpath = ("%s/%s" % (destination, f))
        if os.path.isdir(sourcepath):
            copydir(sourcepath, destinationpath)
        elif f != ".DS_Store" and f[-4:] != ".nov" and not os.path.isfile(destinationpath):
            shutil.copyfile(sourcepath, destinationpath)
            shutil.copystat(sourcepath, destinationpath)
            copied += 1
            copied_per_second += 1
            destination_count += 1
            file_size = os.path.getsize(sourcepath)
            bytes_transferred += file_size
            if copied == 1:
                print("Copying. Please wait...")
                elapsed_time = time.time() - starttime
            fulltime = str(datetime.datetime.now())
            current_time = str(fulltime.split()[1].split(".")[0])

            if time.time() > next_output:
                next_output += 1
                copied_per_second_average.append(copied_per_second)

                print(current_time)
                print(f)
                #print("%s files copied" % copied)
                print("%s files (%.2f MB) transferred at %d KB/s" % (copied, float((bytes_transferred / (1024*1024))), ((bytes_transferred/1024)//(time.time() - starttime))))
                print("%s files (%.2f MB) remaining" % (int((source_count - destination_count)), float((dir_size - bytes_transferred) / (1024*1024))))
                files_per_second = int(sum(copied_per_second_average)/len(copied_per_second_average))
                copied_per_second = 0
                seconds_remaining = int(source_count - destination_count) / files_per_second
                #print("%s COPIED" % copied)
                #print("%s REMAINING" % (int(source_count - destination_count)))
                percentage = copied / (copied + (int(source_count - destination_count))) * 100
                print("%.1f%% completed" % percentage)

                if seconds_remaining > 60:
                    print("Approximately %s minutes and %s seconds remaining" % (int(seconds_remaining//60), int(seconds_remaining % 60)))
                else:
                    print("Approximately %s seconds remaining" %int(seconds_remaining))
                print()



copied = 0
bytes_transferred = 0
source_size = 0
destination_size = 0
source_count = 0
destination_count = 0
copied_per_second_average = []
copied_per_second = 0

sourcedirectory = input("Enter the source please: ")
destinationdirectory = input("Enter the destination please: ")
print()
print("Counting source files...")
my_source_size = get_source_size(sourcedirectory)

print("Counting destination files...")
my_destination_size = get_destination_size(destinationdirectory)

dir_size = my_source_size - my_destination_size
starttime = time.time()
next_output = time.time() + 1
copydir(sourcedirectory, destinationdirectory)
finaltime = time.time() - starttime

print()
print("\nAll done.")

if copied == 0:
    print("The two directories are already identical.")
else:
    print("Copy operation took %sm and %ss" % (int(finaltime//60), int(finaltime % 60)))
    print("%s files copied" % copied)
    print("%.2f MB transferred" % float((bytes_transferred / (1024*1024))))
    print("Average data rate was %d KB/s" % ((bytes_transferred/1024)//(time.time() - starttime)))
