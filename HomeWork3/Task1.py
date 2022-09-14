# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

def fill_list(numbers):
    for i in range(n):
        numbers.append(int(random.randint(-10, 10)))
    return numbers

def print_sum_odd_pozition(numbers):
    sum = 0
    index = 0
    while index < len(numbers):
        if index % 2 != 0:
            sum += numbers[index]
        index += 1
    print(f'Сумма чисел на нечетных позициях равна {sum}')

n = int(input('Введите количество чисел и мы найдем произведение пар: '))

numbers = []

print(fill_list(numbers))
print_sum_odd_pozition(numbers)
