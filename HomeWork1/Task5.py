# Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

def distant(x1, y1, x2, y2):
    sum = (x2 - x1)**2 + (y2 - y1)**2
    result = math.sqrt(sum)
    return result

print('Введите координаты точки A(x,y)')
x1 = int(input('x: '))
y1 = int(input('y: '))
print('Введите координаты точки B(x,y)')
x2 = int(input('x: '))
y2 = int(input('y: '))
print(f'Расстояние от точки A до точки B: {round(distant(x1, y1, x2, y2), 2)}')