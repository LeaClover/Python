# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и
# меньшее число. В качестве символа-разделителя используйте пробел.

def max_min(str):
    str_list = str.split(sep=' ')
    numbers = []
    for i in str_list:
        numbers.append(int(i))
    max = numbers[0]
    min = numbers[0]
    i = 0
    while i < len(numbers):
        if numbers[i] > max:
            max = numbers[i]
        if numbers[i] < min:
            min = numbers[i]
        i += 1
    maxmin = [max, min]
    for i in maxmin:
        print(i, end=" ")


str = input('Введите набор чисел через пробел: ')

print(f'Большее и меньшее числа соответственно равны: ')
max_min(str)

# Второй вариант
# stroka = '3, 4, 5, 6'
# x = stroka.split(', ')
# for i in range(len(x)):
#     x[i] = int(x[i])
# max_list = x[0]
# min_list = x[0]
# for i in x:
#     if max_list < i:
#         max_list = i
#     if min_list > i:
#         min_list = i
# print(max_list, min_list)
