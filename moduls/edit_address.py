from moduls import AddAddresses

add = AddAddresses.addAddresses

coord = []
edit_file = 'Addresses.txt'

def open_file():
    with open(edit_file, 'r', encoding = 'utf-8') as opnfile:
        x = opnfile.read()
        x = x.strip()
        x = x.replace('\ufeff', '')
        try:
            dict_file = eval(x)
        except SyntaxError:
            print('Документ ',edit_file, ' пустой')
            dict_file = {}
        
    return dict_file

def show_addresses(dict_file):
    for key, val in dict_file.items():
        print(key)
        print(val)

def dell_address(dict_file):
    with open(edit_file, 'w', encoding = 'utf-8') as opnfile:
        try:
            num = input('Впиши через пробел номера адресов для удаления: ')
            num_dell = num.split()
            num_dell = list(map(int, num_dell))
            num_dell = sorted(num_dell)
            num_dell = [i for num, i in enumerate(dict_file) if num in num_dell]
            list(map(dict_file.pop,num_dell))
            print('Удалено: ', num_dell)
        except KeyError:
            print('Указанного адреса нет в списке. Возможно допущена ошибка')
        opnfile.write(str(dict_file))

def main():
    print('Эта программа предназначена для редактирования списка адресов '
          'программы Matreshka.\n')
    comand = ('Список команд: \n'
          '1 - вывести все адреса с координатами.\n'
          '2 - добавить адреса.\n'
          '3 - удалить адрес.\n'
          '4 - завершить программу\n')
    
    x = '0'
    while x != '4':
        print(comand)
        x = input('Введите номер команды: ')
        read_dic = open_file()
        if x == '1':
            key = [i for i in read_dic]
            for num, val in enumerate(key):
                print('{}. Название улицы: {: <20}'.format(num, val))
##                print ('Область поиска: {:<}'.format(str(val)))
                print('{:-<60}'.format(''))
        elif x == '2':
            add()
        elif x == '3':
            dell_address(read_dic)  

if __name__ == '__main__':
    main()
