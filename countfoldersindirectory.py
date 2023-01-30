### https://www.positronx.io/python-count-the-number-of-files-and-directories/

import os

#define the app folder to work in
APP_FOLDER = "E:/"
totalFiles = 0
totalDir = 0


for base, dirs, files in os.walk(APP_FOLDER):
    print('Searching in ' + base)
    for directory in dirs:
        totalDir += 1
    for Files in files:
        totalFiles += 1

print('Total number of files', totalFiles)
print('Total number of directories', totalDir)
print('Total: ', (totalDir + totalFiles))