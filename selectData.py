# program to select files with a specific number in its name and copy to other directory
#libraries
import os
import shutil
fileIdNumbers = [4,9,15,18,25,31,37,38,39,40,41,42,43,44,46,47,48,51,53,
54,56,67,70,71,76,82,83,87,88,91,92,96,99,102,104,110,111,122,128,133,
135,136,138,139,140,141,143,145,147,148,151,153,154,158,159,164,174,176,
181,182,183,184,186,187,190,192,193,194,195,196,197,198,200,203,207,208,
210,212,213,214,216,217,218,219,221,223,226,232,233,236,242,243,246,247,
248,249,252,253,255,256,258,260,261,262,263,264,266,267,268,269,270,271,
272,273,274,275,276,282,286,288,289,292,293,294,295,296,297,298,299,204,
366,367,370,375,376,377,381,384,385,300,301,302,325,326,327,328,329,330,
335,336,338,340,341,342,344,345,346,348,349,350,351,352,353,354,357,
359,361,363,365,387,388,389,391,395,397,403,404,409,412,413,433,439,343]
# Files
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
dst = '/home/jjsantiago/data/spectraData/selectedData' #destination directory
for number in fileIdNumbers:
    for file in files:
        if file.find('_' + str(number) + '.') > -1:
            shutil.copy('/home/jjsantiago/data/spectraData/cheminfo/'+ str(file), path)
            selectedFiles.append(file)
print('Action completed successfully')