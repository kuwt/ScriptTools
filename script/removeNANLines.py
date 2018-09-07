import os

def removeNANLines(inputfilepath, outputfilepath):
    lines = tuple(open(inputfilepath, 'r'))

    updatelines = []
    for line in lines:
        if "nan" not in line:
            updatelines.append(line)

    outfile = open(outputfilepath, 'w')
    for line in updatelines:
        outfile.write("%s\n" % line)

if __name__ == '__main__':
    infilepath = r"D:\sourcecode\unre face scanner\faceScanner\CalibrationV1\Calibration\pointcloud.txt"
    outfilepath = r"pc.txt"
    removeNANLines(infilepath,outfilepath)