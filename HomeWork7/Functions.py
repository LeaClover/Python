def search(search_data, phone_data):
    flag = 0
    if flag == 0:
        for line in phone_data:
            if search_data in line:
                print(line)
                flag = 1
    if flag == 0:
        print('Таких данных нет!')
            