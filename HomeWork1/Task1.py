# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

n = int(input('Введите цифру дня недели и мы проверим выходной ли это: '))
if n == 6 or n == 7:
    print('Выходной!!!')
elif n < 6 and n >= 1:
    print('Будний день...')
else:
    print('Введено неверное значение!!!')
