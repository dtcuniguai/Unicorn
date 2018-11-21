# use in window&Unix
import os

def getFiles(path):
    fileArray = []
    for root, dirs, files in os.walk(path, False):
        for name in files:
            fileArray.append(name)
    return fileArray


print(getFiles("../test"))
