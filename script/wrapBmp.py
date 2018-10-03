import os
import shutil
def wrapBmp(dir):
    imagePackDir = "."
    for num in range(1,2000):
        tempDir = str(num)
        if not os.path.exists(tempDir):
            os.makedirs(tempDir)
            imagePackDir = tempDir
            break
    for dirname, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            if "bmp" in filename:
                dstPath = imagePackDir + "\\" + filename
                shutil.move(filename, dstPath)

if __name__ == '__main__':
    cwd = os.getcwd()
    wrapBmp(cwd)