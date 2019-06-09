#!/usr/bin/env python

#сжимает фото
#принимает путь к фото, где и под каким именем сохранить
import os
from PIL import Image

def compres_pic(pic, path_saved):
    folder = os.path.split(path_saved)[0]
    if not os.path.isdir(folder):
        os.makedirs(folder)
    pic_opn = Image.open(pic)
    rpic = pic_opn.size
    if rpic[0] > 3500:
        rpic = int(rpic[0] * 0.3), int(rpic[1] * 0.3)
    elif rpic[0] < 1200:
        pass
    else:
        rpic = int(rpic[0] * 0.5), int(rpic[1] * 0.5)
    print(' {:~^70} '.format(os.path.split(pic)[1]))
    pic_opn.thumbnail(rpic)

    date_time = pic_opn._getexif()[306] #получение даты
    date = date_time[:10]
    time = date_time[10:]
    time = time.replace(':', '-')
    date = date.replace(':', '')
    date = (date[6:8] + '-' + date[4:6] + '-' + date[:4]
            + time) #формат dd-mm-yyyy hh-mm-ss
    print(date)
    pname = str(date) + ' ' + os.path.split(path_saved)[1]
##  Добавляем дату в имя файла  
    path_saved = os.path.join(os.path.split(path_saved)[0], pname)
    pic_opn.save(path_saved, optimize = True)

    return path_saved

if __name__ == "__main__":
    import os

    count = 0
    pic = ''
    pic_saved = ''
    if not os.path.isdir('Сжатые фото'):
        os.mkdir('Сжатые фото')
        
    for root, direct, files in os.walk(os.getcwd()):
        for file in files:
            if file.lower().endswith('jpg') or file.lower().endswith('jpeg'):
                pic = (os.path.join(root, file))
                
                name = (os.path.split(root)[1] +
                        ' (' + str(count) + ')' + '.jpg')
                pic_saved = (os.path.join(
                    os.path.join(os.getcwd(), 'Сжатые фото'), name))
                count +=1
                if not 'Сжатые фото' in pic:
                    compres_pic(pic, pic_saved)


    
