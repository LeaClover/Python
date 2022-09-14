# 2. Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.

import random

a = list()
for i in range(10):
    a.append(int(random.randint(1, 10)))
print(a)

b = int(input('Введите число: '))

for i in a:
    if i == b:
        print('yes')
        break
else:
    print('no')
