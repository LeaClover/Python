from Text import answer1, answer2, answer3, repeat

def start():
    print('Привет, это телефонный справочник. Что вы хотите сделать?\n')
    print('1 - внести новые данные\n2 - получить уже существующие данные\n3 - экспорт из файла в справочник')
    answer = int(input('Введите номер команды: '))
    if answer == 1:
        answer1()
        answer = repeat()
        if answer == 1:
            start()
        elif answer == 2:
            exit()
    elif answer == 2:
        answer2()
        answer = repeat()
        if answer == 1:
            start()
        elif answer == 2:
            exit()
    elif answer == 3:
        answer3()
        answer = repeat()
        if answer == 1:
            start()
        elif answer == 2:
            exit()
    else:
        print('Вы ввели неверное значени! Повторите попытку!!!\n')
        start()
