# -*- coding: UTF-8 -*-
from googlesearch import search
import re
import os


def getFiles(path):
    fileArray = []
    for root, dirs, files in os.walk(path, False):
        for name in files:
            fileArray.append(name)
    return fileArray


def searchByGoogle (query): 
    
    url = None
    website = None

# using google search find url
    for j in search(query, num=5, stop=20, pause=1): 
        url = j
        if (re.search(r"dmm.com",j)) :
            website = "dmm.com"
            break
        elif(re.search(r"avgle.com",j)) :
            website = "avgle.com"
            break
        else :
            continue

# format return object
    obj = {}
    obj['website'] = website
    obj['url'] = url
    obj['fileName'] = query


    return obj


files = getFiles('./')

for file in files:
    print(searchByGoogle(file))