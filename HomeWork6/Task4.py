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