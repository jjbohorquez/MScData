# program to select files with a specific number in its name and copy to other directory. 
#libraries
import os
import shutil
#Define the file numbers to copy.
fileIdNumbers = [4,9,15,18,25,31,37,38,39,40,41,42,43,44,46,47,48,51,53,
54,56,67,70,71,76,82,83,87,88,91,92,96,99,102,104,110]
# Give the specific file path to the program (source files directory path)
#You need to change the paths depending on your files location.
files = os.listdir('/home/jjsantiago/data/spectraData/cheminfo')
print('Introduce new directory name')
newDirectory = input()
# path with new directory
path = '/home/jjsantiago/data/spectraData/' + newDirectory
# define the access rights
access_rights = 0o755
try:
    os.mkdir(path, access_rights)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s" % path)

selectedFiles = []
src = '/home/jjsantiago/data/spectraData/cheminfo' #source of the data
for number in fileIdNumbers:
    for file in files:
        if file.find('_' + str(number) + '.') > -1:
            shutil.copy('/home/jjsantiago/data/spectraData/cheminfo/'+ str(file), path)
            selectedFiles.append(file)
print('Action completed successfully')
