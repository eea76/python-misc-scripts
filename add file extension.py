import os

path = "/Library/Application Support/East West/ProductChunks/"

for file in os.listdir(path):
    if not file.endswith(".key") and not file.endswith(".ewl"):
        os.rename(path + file, path + file + ".ewc")
