# 3. Задайте два числа. Напишите программу, которая
# найдёт НОК (наименьшее общее кратное) этих двух чисел.

n = int(input('Введите n: '))
m = int(input('Введите m: '))
count = n * m
while n != m:
	if n > m:
		n = n - m
	else:
		m = m - n
print(count/n)

# Второй вариант
# a = int(input())
# b = int(input())
# p = a * b

# while a != 0 and b != 0:
#     if a > b:
#         a = a % b
#     else:
#         b = b % a
# nod = a + b
# nok = p // nod
# print(nok)
