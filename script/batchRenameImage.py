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

###################################################################
folderpath = input('Enter a folder path: ')
startIdx = input('Enter Index for the first image: ')
ignorelist = ["templ","mask"]

os.chdir(folderpath)

#find all the img files
listExt = ["png","jpg","bmp"]
listfiles = []
Tmplistfiles = list_files1(folderpath,listExt)
for filename in Tmplistfiles:
    isAppend = 1
    for ignorename in ignorelist:
        if ignorename in filename:
            isAppend = 0
    if isAppend:
        listfiles.append(filename)

#rename to tmp first
currentIdx = 0
listfilesRename = []
for filename in listfiles:
    extension = os.path.splitext(filename)[1]
    newName = "Rename_TMP_" + str(currentIdx) + extension
    os.rename(filename, newName)
    currentIdx += 1
    listfilesRename.append(newName)

currentIdx = int(startIdx)
for filename in listfilesRename:
    extension = os.path.splitext(filename)[1]
    newName = str(currentIdx) + extension
    os.rename(filename, newName)
    currentIdx += 1