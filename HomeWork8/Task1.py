# Хакер Василий получил доступ к классному журналу и хочет заменить 
# все свои минимальные оценки на максимальные. Напишите программу, 
# которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1
import random

def fill_list(n, list):
    for i in range(n):
        list.append(random.randint(1, 5))
    return list

def change_mark(list_of_mark):
    for i in range(len(list_of_mark)):
        if list_of_mark[i] >= 4:
            list_of_mark[i] = random.randint(1, 3)
    print(list_of_mark)

n = int(input('Введите количесво оценок: '))
list_of_mark = []
print(fill_list(n, list_of_mark))
change_mark(list_of_mark)
