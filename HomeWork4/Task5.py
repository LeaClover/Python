# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

import Task4

path2 = 'polymonial2.txt'
Task4.pull_in_file(Task4.get_polynomial(Task4.str_coeff, Task4.k), path2)

