# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def quarter(x, y):
    if x > 0 and y > 0:
        return print('I четверть!')
    if x < 0 and y > 0:
        return print('II четверть!')
    if x < 0 and y < 0:
        return print('III четверть!')
    if x > 0 and y < 0:
        return print('IV четверть!')
    elif x == 0 or y == 0:
        return print('Нет такой четверти!')

x = int(input('Введите значение x: '))
y = int(input('Введите значение y: '))
quarter(x, y)