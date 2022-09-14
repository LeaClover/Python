# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

def fill_list(numbers):
    for i in range(n):
        numbers.append(float(round(random.uniform(-10, 10), 2)))
    return numbers

def print_diff_of_minmax_numbers(numbers):
    a = list()
    min = float(numbers[0])
    max = float(numbers[0])
    for i in numbers:
        if i < min:
            min = i
        elif i > max:
            max = i
    a = [min, max]
    print(f'Минимальное и максимальное числа {a}')
    diff = max - min
    print(f'Разница между максимальным и минимальным элементом равна {diff}')

n = int(input('Введите количество чисел и мы найдем произведение пар: '))

numbers = []

print(fill_list(numbers))
print_diff_of_minmax_numbers(numbers)
