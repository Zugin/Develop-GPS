##Программа посылает запрос в виде адреса в яндекс карты и на выходе создает или
##дополняет файл с адресами

import requests
import json
import os

def addAddresses ():
    file_addresses = 'Addresses.txt'
    print('Вводите поочереди необходимые адресса, нажимая ENTER в конце'
          'каждого.\n'
          'Если адрес определился не верно введите "нет" и повторите адрес '
          'с уточнением района или исправив ошибки\n'
          'Для завершения ввода введите "выход"\n')
    city_find = input('Введите город, в котором будем искать адреса: ')

    if os.path.isfile(file_addresses):
        with open(file_addresses, 'r', encoding='utf-8') as openfile:
            gps_dict = openfile.read()
            gps_dict = gps_dict.strip()
            gps_dict = gps_dict.replace('\ufeff', '')
            try:
                gps_dict = eval(gps_dict)
            except SyntaxError:
                print('Ошибка: gps_dict = eval(gps_dict)')
                gps_dict = {}
    
    while True:
        url_in = input('Введите район, улицу, дом\n'
                       '(Пример: Королёв, улица Фрунзе, 4): ')
        if url_in.lower() == 'выход':
            break
        url_in = url_in.replace(' ', '+')
        url = ('https://geocode-maps.yandex.ru/1.x/?format=json&'
               'apikey=303be2a2-5517-4e65-bae7-2628b9cac065&'
               'geocode=' + city_find + '+' + url_in)
        doc = requests.get(url)
        direct = doc.json()

        point = (direct['response']['GeoObjectCollection']
        ['featureMember'][0]['GeoObject']['metaDataProperty']
        ['GeocoderMetaData']['Address']['formatted'])
        start = point.find(city_find)+len(city_find)+2
        point_cut = point[start:]


        lowerCorner = (direct['response']['GeoObjectCollection']
        ['featureMember'][0]['GeoObject']['boundedBy']
        ['Envelope']['lowerCorner']).split(' ')
        lowerCorner1 = [float(lowerCorner[1]), float(lowerCorner[0])]
        
        upperCorner = (direct['response']['GeoObjectCollection']
        ['featureMember'][0]['GeoObject']['boundedBy']
        ['Envelope']['upperCorner']).split(' ')
        upperCorner2 = [float(upperCorner[1]), float(upperCorner[0])]

        lowerCorner2 = [float(lowerCorner1[0]), float(upperCorner2[1])]
        upperCorner1 = [float(upperCorner2[0]), float(lowerCorner1[1])]


        print('Проверьте найденный адрес:\n{}\n'
              'Если верно нажмите ENTER если, нет впишите "нет" '
              'и уточните адрес'.format(point))
        check_address = input()
        if check_address.lower() == 'нет':
            continue

        if point in ([point for i in gps_dict  if point in i[0]]):
            print('Такой адресс уже есть в базе')
            continue
        gps_dict[point_cut] = [upperCorner1, upperCorner2, lowerCorner1, lowerCorner2]
    with open(file_addresses, 'w', encoding='utf-8') as openfile:
        openfile.write(str(gps_dict))

if __name__ == '__main__':
    addAddresses()
