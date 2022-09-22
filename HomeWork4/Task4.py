# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def list_of_coefficients(k):
    coeff = list()
    for i in range(k+1):
        coeff.append(int(random.randint(0, 100)))
        if coeff[0] == 0:
            coeff[0] = random.randint(1, 100)
    return coeff

def get_polynomial(coeff_list, k):
    view = ''
    for i in range(k+1):
        if k == 1:
            view = view + coeff_list[i] + '*x' + ' + '
        elif k == 0:
            view = view + coeff_list[i] + ' = 0'
        else:
            n = str(k)
            view = view + coeff_list[i] + '*x^' + n + ' + '
        k = k - 1
    return view

def pull_in_file(str, path):
    data = open(path, 'w+')
    data.write(f'Polynomial with degree k = {k}: ')
    data.write(str)
    data.close()

k = int(input('Введите натуральную степень многочлена: '))
coeff = list_of_coefficients(k)
print(coeff)
str_coeff = list()
for i in coeff:
    str_coeff.append(str(i))
print(str_coeff)

path1 = 'polymonial1.txt'
pull_in_file(get_polynomial(str_coeff, k), path1)


## Еще вариант
# from random import randint as rd


# k = int(input())

# arr = list()
# for i in range(k, 0, -1):
#     x = rd(-100, 100)
#     if x > 0 and i != k:
#         arr.append(f'+{x}*x^{i}')
#     else:
#         arr.append(f'{x}*x^{i}')
        
# x = rd(-100, 100)
# if x > 0 and i != k:
#     arr.append(f'+{x}')
# else:
#     arr.append(f'{x}')
# arr.append(' = 0')
# print(''.join(arr))


## Еще один вариант

# import random

# k = int(input('Введите степень: '))
# cof = []
# for i in range(k + 1):
#     k = random.randint(0, 100)
#     cof.append(str(k))
    
# print(cof)
# arr = []
# utf = {0: "\u2070", 1: "\u00B9",2: "\u00B2",3: "\u00B3", 4: "\u2074", 5: "\u2075",
#        6: "\u2076", 7: "\u2077", 8: "\u2078", 9: "\u2079"}
# for i in range(len(cof) - 1, -1, -1):
#     if i <= 9:
#         arr.append('x' + utf[i] + "+")
#     if i > 9:
#         a = i // 10
#         b = i % 10
#         arr.append('x'+utf[a]+utf[b]+"+")
# arr.append('x+')
# arr.append('')
# print(arr)
# arr_new = []

# for i in range(len(cof)):
#     arr_new.append(cof[i] + arr[i])
# print(arr_new)

# exs = "".join(arr_new)
# print(exs)

# data = open('file2.txt', 'w', encoding='utf-8')
# data.write(exs)
# data.close()

