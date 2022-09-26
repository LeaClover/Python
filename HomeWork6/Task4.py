# Все равны как на подбор

def same_by(characteristic, objects):
    flag = False
    if bool(objects) == False:
        flag = True
    else:
        if characteristic(objects[0]) == 0:
            for i in objects:
                if characteristic(i) == 0:
                    flag = True
                else:
                    flag = False
                    break
        else:     
            for i in objects:  
                if characteristic(i) == 1:
                    flag = True
                else:
                    flag = False
                    break
    return flag

values = []
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('diff')

# Списочное решение
# def same_by(characteristic, object):
#     list_1 = [characteristic(el) for el in object]
#     return len(object) == list_1.count(0)


# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')


# Еще один вариант
# def same_by(characteristic, object):
#     return len(object) == [characteristic(el) for el in object].count(0)

# values = []
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('diff')
