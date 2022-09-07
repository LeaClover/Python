# Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def check(x, y, z):
    f1 = not(x or y or z) 
    f2 = not x and not y and not z
    if f1 == f2:
        print('Утверждение истинно!')
    else:
        print('Утверждение ложно!')
    
x = int(input('Введите значение x: '))
y = int(input('Введите значение y: '))
z = int(input('Введите значение z: '))

check(x, y, z)


# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             print((not(x or y or z)) == (not(x) and not(y) and not(z)))
