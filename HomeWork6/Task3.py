# Пам парам

def check_rifm(poem):
    list_of_vowel = ['а', 'у', 'е', 'ы', 'о', 'э', 'я', 'и', 'ю', 'ё']
    check_list = poem.split()
    list_of_count = []
    count = 0
    for el in check_list:
        for i in el:
            for x in list_of_vowel:
                if i == x:
                    count += 1
        list_of_count.append(count)
        count = 0
    if len(set(list_of_count)) == 1:
        print('Парам пам-пам!')
    else:
        print('Пам парам...')

poem = input('Введите стихотворение: ')
check_rifm(poem)
