# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

def fill_list(numbers):
    for i in range(n):
        numbers.append(int(random.randint(-10, 10)))
    return numbers

def print_product_of_two(numbers):
    numbers_of_product = list()
    index = 0
    mid = int(len(numbers)/2)
    if len(numbers)%2 == 0:
        while index < mid:
            numbers_of_product.append(int(numbers[index] * numbers[len(numbers) - index - 1]))
            index += 1
    elif len(numbers)%2 == 1:
        while index <= mid:
            numbers_of_product.append(int(numbers[index] * numbers[len(numbers) - index - 1]))
            index += 1
    print(f'Сумма чисел на нечетных позициях равна {numbers_of_product}')

n = int(input('Введите количество чисел и мы найдем произведение пар: '))

numbers = []

print(fill_list(numbers))
print_product_of_two(numbers)

# Еще вариант
# list_1 = [3, 2, 4, 5, 6, 7]
# # 3 * 6 = 18
# # 2 * 5 = 10
# # 4 * 4 = 16
# len_list = 0
# if len(list_1) % 2 == 0:
# len_list = len(list_1) // 2
# else:
# len_list = len(list_1) // 2 + 1

# for i in range(len_list):
# print(list_1[i] * list_1[len(list_1) - 1 - i])