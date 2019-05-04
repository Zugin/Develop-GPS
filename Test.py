import requests
import json
import os
def addAddresses ():

    gps_ls = []
    while True:
        url_in = input('Введите адрес: ')
        if url_in.lower() == 'выход':
            break
        url_in = url_in.replace(' ', '+')
        url = ('https://geocode-maps.yandex.ru/1.x/?format=json&'
               'apikey=303be2a2-5517-4e65-bae7-2628b9cac065&'
               'geocode=' + url_in)
        doc = requests.get(url)
        direct = doc.json()

        point = (direct['response']['GeoObjectCollection']
        ['featureMember'][0]['GeoObject']['Point']['pos']).split(' ')
        point = ''.join(point[1] + ' ' + point[0])

        lowerCorner = (direct['response']['GeoObjectCollection']
        ['featureMember'][0]['GeoObject']['boundedBy']
        ['Envelope']['lowerCorner']).split(' ')
        lowerCorner = ''.join(lowerCorner[1] + ' ' + lowerCorner[0])

        upperCorner = (direct['response']['GeoObjectCollection']
        ['featureMember'][0]['GeoObject']['boundedBy']
        ['Envelope']['upperCorner']).split(' ')
        upperCorner = ''.join(upperCorner[1] + ' ' + upperCorner[0])

        print('point: ', direct)
        print('lowerCorner: ',lowerCorner)
        print('upperCorner: ', upperCorner)

        if os.path.isfile('GPS_Points.txt'):
            with open('GPS_Points.txt', 'r+') as openfile:
                f = openfile.read()
                f = eval(f)
                if point in ([point for i in f  if point in i[0]]):
                    print('Такой адресс уже есть в базе')
                else:
                    gps_ls.append([point, lowerCorner, upperCorner])
                    openfile.write(str(gps_ls))
        else:
            with open('GPS_Points.txt', 'w') as openfile:
                gps_ls.append([point, lowerCorner, upperCorner])
                openfile.write(str(gps_ls))

if __name__ == '__main__':
    addAddresses()
