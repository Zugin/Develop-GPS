#!/usr/bin/env python

import os

def get_pic(foldername): #список фото с путями
    if foldername in os.listdir():
        dir_photo = os.path.join(os.getcwd(), foldername)
        dict_photo = []
        #поиск всех фото в папке '/photo'
        for root, directories, files in os.walk(dir_photo):
            for file in files:
                if file.lower().endswith('jpg') or file.lower().endswith('jpeg'):
                    dict_photo.append(os.path.join(root, file))
        return dict_photo
        
    else:
        os.mkdir(foldername)
        print(r'Загрузите в папку "photo" (находится рядом с программой)'
                ' фотографии для переименовывания')
        return None

if __name__ == '__main__':
    foldername = 'photo'
    ls_pic = get_pic(foldername)
    print(ls_pic)
