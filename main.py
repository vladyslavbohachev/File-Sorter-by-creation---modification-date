import os
import time
import shutil

dirpath = 'X:/'
creationdatefolder = 'X:/'

directoryList = [creationdatefolder]
for items in directoryList:
    os.makedirs(items, exist_ok=True)

for root, dirs, files in os.walk(dirpath):
        if dirpath is None:
            exit(0)
        else:
            for filename in files:
                if filename.endswith('.xml'):
                    modificationTime = time.strftime('%d.%m.%Y', time.localtime(os.path.getmtime(os.path.join(dirpath, filename))))
                    dirlist = [modificationTime]
                    for items in dirlist:
                        os.makedirs(dirpath+items, exist_ok=True)
                    shutil.move(os.path.join(dirpath, filename), os.path.join(creationdatefolder + str(modificationTime), filename))
