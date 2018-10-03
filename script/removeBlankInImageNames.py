import os
import shutil


def removeBlankInName(dir):
    for dirname, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            tempFileName = filename
            tempFileName.replace(" ","")
            os.rename(filename, tempFileName)

if __name__ == '__main__':
    cwd = os.getcwd()
    removeBlankInName(cwd)