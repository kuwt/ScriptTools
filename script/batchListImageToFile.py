import os
import glob

def list_files1(directory, listextension):
    RetList = []
    for f in os.listdir(directory):
        isAppend = 0
        for extension in listextension:
            if f.endswith('.' + extension):
                isAppend = 1
        if isAppend:
            RetList.append(f)
    return RetList

###############################################################
folderpath = input('Enter a folder path: ')
priorlist = ["templ","mask"]

os.chdir(folderpath)

#find all the img files
listExt = ["png","jpg","bmp"]
priorfiles = []
remainfiles = []
Tmplistfiles = list_files1(folderpath,listExt)
for filename in Tmplistfiles:
    isIncludePrior = 0
    for priorname in priorlist:
        if priorname in filename:
            isIncludePrior = 1
    if isIncludePrior:
        priorfiles.append(filename)
    else:
        remainfiles.append(filename)


for filename in priorfiles:
