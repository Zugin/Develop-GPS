#!/usr/bin/env python

import os

#определяет попадают ли координаты в заданную область
#принимает словарь изимени фото, широты и долготы

def find_gps(gps):
    target = [1, 1, 0, 0, 0, 1, 0,1]
    DD = {}
    dd = {}
    count = 0
    ret = []
    ls_key_g = []
    ls_key_t = []
    
    
    with open('Addresses.txt', 'r', encoding = 'utf-8') as openfile:
        x = openfile.read()
        x = x.strip()
        x = x.replace('\ufeff', '')
        targ = eval(x)

    for key_g, g in gps.items(): #итерации по фото
        ls_key_g.append(key_g)
        for key_t, t in targ.items():
            ls = []
            for val_t in t:
                ls.append(check_gps(g[0], val_t[0]))
            if ls == target[:4]:
                ls = []
                for val_t in t:
                    ls.append(check_gps(g[1], val_t[1]))
                if ls == target[4:]:
                    pic = os.path.join(os.getcwd(),'Имена по GPS')
                    pic = os.path.join(pic,key_t)
                    pic = os.path.join(pic, key_t + '(' + str(count) + ')'
                                        +  '.jpg')
                    
                    ret.append((key_g, pic))
                    ls_key_t.append(key_g)
                    count += 1
                    
## вывод на экран списка фото которые не удалось определить 
    coun = 0
    for i, val in gps.items():
        if not i in ls_key_t:
            print(' {:-^70}'.format(os.path.split(i)[1]))
            print('GPS координаты: {}, {}'.format(val[0], val[1]))
            coun += 1
    if coun == 0:
        print(('\n{:-^70}\n').format('Удалось определить место у всех фото'))
        
    return ret
                    
                
        

def check_gps(val_g, val_t):
    target = [1, 1, 0, 0, 0, 1, 0,1]
    r = 0
    
    if val_g > val_t:
        r = 0
##        print('val_g: {:<10} > val_t: {:<10} {:-^5}'.format(val_g, val_t, r))
    else:
        r = 1
##        print('val_g: {:<10} < val_t: {:<10} {:-^5}'.format(val_g, val_t, r))
    return r
 
if __name__ == '__main__':
    gps = [58.599386, 49.648717]
    find_gps(gps)
