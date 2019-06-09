#!/usr/bin/env python
import os
import zipfile

def zip_folder(name_zip, file):

    path = os.path.split(file)[1]
    
    if not zipfile.is_zipfile(name_zip + '.zip'):
        with zipfile.ZipFile(name_zip + '.zip', 'w') as zfile:
            zfile.write(file, path)
    else:
        with zipfile.ZipFile(name_zip + '.zip', 'a') as zfile:
            if path not in zfile.namelist():
                zfile.write(file, path)        

if __name__ == '__main__':
    zip_folder(name_zip, file)
