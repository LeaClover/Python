# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

def quarter(n):
    if n == 1:
        return print('Диапозон координат I четверти: x > 0 и y > 0!')
    if n == 2:
        return print('Диапозон координат II четверти: x < 0 и y > 0!')
    if n == 3:
        return print('Диапозон координат III четверти: x < 0 и y < 0!')
    if n == 4:
        return print('Диапозон координат IV четверти: x > 0 и y < 0!')
    elif n < 1 or n > 4:
        return print('Неверное значение!')

n = int(input('Введите номер четверти от 1 до 4: '))
quarter(n)
