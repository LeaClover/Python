# https://www.eolymp.com/ru/problems/854

# Дружественные числа

# import random

# def freandly_numbers(m, n):
#     index1 = 0
#     count = 0
#     d1 = list()
#     d2 = list()
#     while m + index1 < n:
#         index2 = 0
#         while m + index1 < n - index2:
#             index = 1
#             d1.clear()
#             while index < m + index1:
#                 if (m + index1)%index == 0:
#                     d1.append(index)
#                 index += 1
#             sum1 = 0
#             for i in d1:
#                 sum1 = sum1 + i
#             index = 1
#             d2.clear()
#             while index < n - index2:
#                 if (n - index2)%index == 0:
#                     d2.append(index)
#                 index += 1
#             sum2 = 0
#             for j in d2:
#                 sum2 = sum2 + j   
#             if (m + index1) == sum2 and (n - index2) == sum1:
#                 print(f'{m + index1} {n - index2}')
#                 count += 1
#             index2 += 1
#         index1 += 1
#     if count == 0:
#         print('Absent')

# print('Поиск дружественных чисел!')
# m = int(input('Введите начало промежутка: '))
# n = int(input('Введите конец промежутка: '))
# freandly_numbers(m, n)

# Второй вариант

n = int(input('Введите 1-ое число: '))
m = int(input('Введите 2-ое число: '))
d = {}
resultArray = list()

for i in range(n, m + 1):
    summa = 0
    for j in range(1, round(i / 2) + 1):
        if i % j == 0:
            summa += j
    d[i] = summa
for i in d:
    for j in d:
        if d[i] == j and d[j] == i and i != j and (i, j) not in resultArray and (j, i) not in resultArray:
            resultArray.append((i, j))
for i in resultArray:
    print(*i)


