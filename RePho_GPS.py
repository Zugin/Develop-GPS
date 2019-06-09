#!/usr/bin/env python

from moduls import stopwatch
from moduls import ListPic
from moduls import comprespic
from moduls import GetGps
from moduls import gpsintarget
from moduls import MakeZip
from moduls import edit_address

import sys
import os


zipname = 'Матрешка'

def make_addresses():
    if not os.path.isfile('Addresses.txt'):
        with open('Addresses.txt', 'w', encoding = 'utf-8') as opfile:
            address = {'Атак.Королев ленина 25': [[55.917562, 37.803921], [55.917219, 37.809586], [55.914706, 37.803599], [55.914141, 37.810777]], 'Атак.Широкая ул 29': [[55.889037, 37.673679], [55.889217, 37.681457], [55.885787, 37.672788], [55.885564, 37.68238]], 'Атак.Московская ул., 14, Химки': [[55.896174, 37.445119], [55.896438, 37.452693], [55.892348, 37.444346], [55.892300, 37.454453]], 'Атак.ул. Химки, Молодежная 12': [[55.884553, 37.412016], [55.884782, 37.420213], [55.881761, 37.412467], [55.881954, 37.420696]], 'Атак.мкр, Большево, ул. Пушкинская, д.17, 1 этаж, Королёв': [[55.933752, 37.837074], [55.934173, 37.84488], [55.930188, 37.836394], [55.930194, 37.845277]], 'Атак.ул. Лётчика Бабушкина, 15': [[55.866148, 37.669612], [55.864412, 37.674766], [55.863401, 37.672406], [55.863335, 37.674981]], 'Атак.Авангардная ул., 3': [[55.845771, 37.484836], [55.846362, 37.495522], [55.840169, 37.484364], [55.840169, 37.498827]], 'Атак.ул. Ленина, 25, Королёв': [[55.919743, 37.798274], [55.919983, 37.815741], [55.911782, 37.798704], [55.910989, 37.815913]], 'Атак.Олимпийский пр-т., 13 Мытищи': [[55.922244, 37.758547], [55.922443, 37.767323], [55.918373, 37.756777], [55.917855, 37.768514]], 'Атак.Староватутинский пр-д, 12 строение 1': [[55.879206, 37.664155], [55.879143, 37.679792], [55.870002, 37.655788], [55.869021, 37.686711]], 'Атак.Атак.Ясный пр-д, 19 строение 2': [[55.879736, 37.608853], [55.880183, 37.626422], [55.872511, 37.608584], [55.872467, 37.62749]], 'Атак.ул. Адмирала Макарова, 6 строение 3': [[55.839579, 37.484243], [55.840246, 37.498661], [55.832466, 37.484363], [55.831389, 37.500012]], 'Атак.Панфиловский пр., корпус 1801, Зеленоград': [[55.980065, 37.158226], [55.980496, 37.167439], [55.975054, 37.157411], [55.974827, 37.168454]], 'Атак.Яблоневая аллея, корпус 313а': [[55.999989, 37.214495], [56.000226, 37.224268], [55.995837, 37.212914], [55.99521, 37.223811]], 'Атак.ул. Снежная, 16': [[55.853879, 37.641728], [55.854015, 37.650675], [55.848958, 37.639387], [55.848158, 37.652414]], 'Атак.ул. Печорская, 3': [[55.863651, 37.669133], [55.863482, 37.672191], [55.862332, 37.669284], [55.862199, 37.673468]], 'Атак.Старое Дмитровское ш., 15, Долгопрудный': [[55.964615, 37.526655], [55.965047, 37.533575], [55.960711, 37.524734], [55.960711, 37.524734]], 'Атак.Час Пик МКАД 87 км (внутр.), 8': [[55.900127, 37.625589], [55.900223, 37.633282], [55.896566, 37.624517], [55.896356, 37.635344]], 'Атак.Ангарская ул., 13': [[55.876699, 37.509918], [55.877542, 37.519531], [55.873340, 37.508437], [55.872642, 37.519338]], 'Атак.Бибиревская ул., 9': [[55.881352, 37.591571], [55.881472, 37.596925], [55.87877, 37.591625], [55.878234, 37.598781]], 'Атак.Ленинградское ш., 132А': [[55.871503, 37.457326], [55.871966, 37.46372], [55.869528, 37.457594], [55.869365, 37.464675]], 'Атак.ул. Красная Сосна, 2': [[55.851379, 37.678068], [55.851373, 37.6831], [55.848898, 37.67707], [55.848699, 37.6834]], 'Атак.ул. Фрунзе, 4': [[55.924336, 37.819297], [55.924841, 37.82611], [55.921463, 37.81846], [55.921048, 37.826861]], 'Атак.корпус 234 А Зеленоград': [[56.003883, 37.203042], [56.004237, 37.208246], [56.002173, 37.202839], [56.002011, 37.209115]]}
            opfile.write(str(address))

def make_readme():
    if not os.path.isfile('Инструкция.txt'):
        with open('Инструкция.txt', 'w', encoding = 'utf-8') as opfile:
            readme = ('Для переименовывания фото нужно загрузить их в папку "photo", '
                      'ВАЖНО что бы сама программа была рядом с "photo",'
                      'после этого запустить файл "Matreshka". Будет создана папка "Имена по GPS" с '
                      'переименованными фото разложенными по разным папкам, так же создастся'
                      'архив под именем "Матрешка" с фото без папок для отправки по почте.\n'
                      'Что умеет программа:\n'
                      '- переименовывать фото по названию адрессов заранее указаных магазинов\n'
                      '- сжимать фото без видимой потери качества\n'
                      '- упаковывать в архив\n'
                      '- удалять обработанные фото\n'
                      '- раскладывать обработанные фото по папкам с адресами\n'
                      '- редактировать базу адресов\n\n'

                      'Если каким то образом у вас оказалась эта программа и есть вопросы или '
                      'предложения со мной можно связаться по почте Zugin2009@yandex.ru')
            opfile.write(str(readme))
            
        os.startfile('Инструкция.txt')
        sys.exit()
            
with stopwatch.Profiler() as p:
    if not os.path.isdir(os.getcwd()+'/photo'):
        os.mkdir('photo')
    make_addresses()
    make_readme()
    start = input('Если вы ходите отредактировать или добавить адресса\n'
                  'введите 1, если обработать фото ENTER:\n')
    if start == '1':
        edit_address.main()
        sys.exit()
    ls_pic = ListPic.get_pic('photo')
    print('{:=^70}'.format(' нет gps координат в фото '))
    gps_a = GetGps.get_gps1(ls_pic)
    print('{:=^70}'.format(' Не удалось определить фото '))
    place = gpsintarget.find_gps(gps_a)
    print('{:=^70}'.format(' Сжатие файлов '))

    if os.path.isfile(zipname + '.zip'):
        os.remove(zipname + '.zip')
    
    for pic in place:
        psaved = comprespic.compres_pic(pic[0], pic[1])
        MakeZip.zip_folder(zipname, psaved)

##    for pic in place:
##        os.remove(pic[0])
        
    print('\n{:=^70}\n'.format(' Улыбаемся и пляшем '))

input('Нажми Enter для выхода')
