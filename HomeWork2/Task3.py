# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

def divisor(n):
    i = 2
    while i <= n:
        if n%i == 0:
            return i
        i += 1

n = int(input('Введите число N: '))
print(f'Наименьший натуральный делитель: {divisor(n)}')

# Еще вариант
# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0:
#         print(i)
#         flag = False
#     i += 1

