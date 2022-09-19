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
