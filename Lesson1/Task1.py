#    Напишите программу, которая принимает на вход два числа и проверяет, 
#    является ли одно число квадратом другого.
    
#    *Примеры:* 
    
#    - 5, 25 -> да
#    - 4, 16 -> да
#    - 25, 5 -> да
#    - 8,9 -> нет

n = int(input('Введите первое число: '))
m = int(input('Введите первое число: '))
if n == m*m:
    print('да')
elif m == n*n:
    print('да')
else:
    print('нет')

'''
Еще вариант
n = int(input('Введите 1-ое число: '))
m = int(input('Введите 2-ое число: '))
if n == m ** 2 or m == n ** 2:
    print('yes')
else:
    print('no')
'''
