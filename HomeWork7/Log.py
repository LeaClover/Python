from Functions import search

def add_data(surname, name, patronymic, phone_number):
    with open('PhoneBook.txt', 'a+', encoding='utf-8') as phone_book:
        phone_book.write(f'{surname} {name} {patronymic} {phone_number}\n')
    
def read_data(search_data):
    phone_data = open('PhoneBook.txt', 'r', encoding='utf-8')
    search(search_data, phone_data)

def teleport(path):
    with open(f'{path}.txt', 'r', encoding='utf-8') as data:
        for line in data:
            with open('PhoneBook.txt', 'a+') as add:
                add.write(f'{line}')