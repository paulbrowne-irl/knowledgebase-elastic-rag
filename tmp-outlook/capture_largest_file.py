import os
import math

path = 'C:\\'
for foldername, subfolders, filenames in os.walk(path):
    for filename in filenames:
        try:
            filesize = math.floor(os.path.getsize(os.path.join(foldername, filename))/1048576)
            if filesize>1:
                print(foldername + ' , ' + filename+ " , "+str(filesize))
        except FileNotFoundError:
            pass
            #print("Ignoring too long file:"+filename)