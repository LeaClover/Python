# 2. Напишите программу, которая на вход принимает 5 чисел
#     и находит максимальное из них.
    
#    Примеры:
    
#    - 1, 4, 8, 7, 5 -> 8
#    - 78, 55, 36, 90, 2 -> 90

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
c = int(input('Введите четвертое число: '))
d = int(input('Введите пятое число: '))

max = a
if max < b:
    max = b
if max < c:
    max = c
if max < d:
    max = d

print(max)

'''
Eще вариант:

max = -1
for i in range(5):
    n = int(input())
    if max < n:
        max = n
print(max)
'''