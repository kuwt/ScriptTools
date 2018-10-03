import os
import shutil

######################
#   dir to form cali images
#   name of the image in the directory to form cali images
########################
def BatchAddPrefix(dir, prefix):
    for dirname, dirnames, filenames in os.walk(dir):
    # print path to all subdirectories first.
        for subdirname in dirnames:
            srcdir = os.path.join(dirname, subdirname)
            print(srcdir)
            dstdir = prefix + subdirname
            print(dstdir)
            os.rename(srcdir,dstdir)

if __name__ == '__main__':
    cwd = os.getcwd()
    BatchAddPrefix(cwd,"pose_")