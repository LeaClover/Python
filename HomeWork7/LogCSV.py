from Functions import search

def add_data_CSV(surname, name, patronymic, phone_number):
    with open('PhoneBook.csv', 'a+', encoding='utf-8') as phone_book:
        phone_book.write(f'{surname};{name};{patronymic};{phone_number}\n')

def read_data_CSV(search_data):
    phone_data = open('PhoneBook.csv', 'r', encoding='utf-8')
    search(search_data, phone_data)

def teleport_CSV(path):
    with open(f'{path}.csv', 'r', encoding='utf-8') as data:
        for line in data:
            with open('PhoneBook.csv', 'a+') as add:
                add.write(f'{line}')
