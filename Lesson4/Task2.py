# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:

# 1) с помощью математических формул нахождения корней квадратного уравнения

# 2) с помощью дополнительных библиотек Python

from cmath import sqrt
import math

def disc(a, b, c):
    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = (-b + math.sqrt(D))/(2*a)
        x2 = (-b - math.sqrt(D))/(2*a)
        print(f'Корней 2: x1 = {round(x1, 2)} и x2 = {round(x2, 2)}')
    elif D == 0:
        x = -b/(2*a)
        print(f'Корень всего 1: x = {round(x, 2)}')
    else:
        print('Корней нет!')
print('Ax^2 + Bx + C = 0')
a = float(input('Введите коэффициент A: '))
b = float(input('Введите коэффициент B: '))
c = float(input('Введите коэффициент C: '))
disc(a, b, c)
