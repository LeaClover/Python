# Напишите программу, которая определит на какое место в шеренге Пете нужно встать, 
# чтобы не нарушить традицию, если заранее известен рост каждого ученика и 
# эти данные уже расположены по невозрастанию (то есть каждое следующее число не больше предыдущего). 
# Если в классе есть несколько учеников с таким же ростом, как у Пети, 
# то программа должна расположить его после них.

import random

n = int(input('Введите количество учеников: '))
students = list(range(1, n+1))

for i in students:
    students[i-1] = random.randint(150, 200)

students.sort(reverse=True)

print(students)

growth = int(input('Введите ваш рост и мы определим вашу позицию среди учеников: '))

count = 1
for i in students:
    if growth <= i:
        count += 1

print(f'Ваша позиция по росту среди учеников расположенных по убыванию равна {count}')

# Второй вариант
# n = int(input())
# arr_rost = list()

# for i in range(n):
#     rost = int(input())
#     arr_rost.append(rost)
    
# # имя_списка.sort()
# # sorted(имя_списка)
# my_rost = int(input())

# j = 1
# for i in arr_rost:
#     if my_rost <= i:
#         j += 1
# print(j)
