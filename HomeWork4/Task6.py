# https://www.eolymp.com/ru/problems/854

# Дружественные числа

import random

def freandly_numbers(m, n):
    index1 = 0
    count = 0
    d1 = list()
    d2 = list()
    while m + index1 < n:
        index2 = 0
        while m + index1 < n - index2:
            index = 1
            d1.clear()
            while index < m + index1:
                if (m + index1)%index == 0:
                    d1.append(index)
                index += 1
            sum1 = 0
            for i in d1:
                sum1 = sum1 + i
            index = 1
            d2.clear()
            while index < n - index2:
                if (n - index2)%index == 0:
                    d2.append(index)
                index += 1
            sum2 = 0
            for j in d2:
                sum2 = sum2 + j   
            if (m + index1) == sum2 and (n - index2) == sum1:
                print(f'{m + index1} {n - index2}')
                count += 1
            index2 += 1
        index1 += 1
    if count == 0:
        print('Absent')

print('Поиск дружественных чисел!')
m = int(input('Введите начало промежутка: '))
n = int(input('Введите конец промежутка: '))
freandly_numbers(m, n)

