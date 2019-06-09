#!/usr/bin/env python

#Выдает словарь из имени фото, пары широта и долгота в виде списка

from os import path
from PIL import Image        

def get_gps1(dict_photo): #получение gps у каждого фото
    gps_ten = []
    gps_all = {}
    
    for pic in dict_photo:
        i = Image.open(pic)
        info = i._getexif()
        try:
            gps = info[34853][2], info[34853][4] #получение широты и долготы
            
            for i in gps:
                #перевод координат в 10-ую систему счисления
                gps_ten.append(round(i[0][0] + i[1][0]/60 +
                                         i[2][0]/(3600*i[2][1]), 6))
            gps_all[pic] = (gps_ten)
            gps_ten = []
    
        except KeyError:
            print(' {:*^70} '.format(path.basename(pic)))
        except TypeError:
            print('информации о фото {:*^42}'.format(path.basename(pic)))
    return gps_all

                
if __name__ == '__main__':    
    d = ['photo/IMG_20190408_135045.jpg',
         'photo/222.jpg']

    print(get_gps1(d))
