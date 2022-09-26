from Log import add_data, read_data, teleport
from LogCSV import add_data_CSV, read_data_CSV, teleport_CSV

def answer1():
    surname = input('Фамилия: ')
    name = input('Имя: ')
    patronymic = input('Отчество: ')
    phone = input('Телефон: ')
    add_data(surname, name, patronymic, phone)
    add_data_CSV(surname, name, patronymic, phone)

def answer2():
    search_data = input('Введите кого мы ищем: ')
    print()
    read_data(search_data)
    read_data_CSV(search_data)

def answer3():
    path = input('Введите имя файла без расширения: ')
    teleport(path)
    teleport_CSV(path)

def repeat():
    answer = int(input('Хотите продолжить?\n1 - да\n2 - нет\n'))
    return answer
    