# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def get_bin(n):
    bin = list()
    while n > 0:
        bin.append(n%2)
        n = n//2
    bin.reverse()
    index = 0
    while index < len(bin):
        print(bin[index], end='')
        index += 1

# Второй вариант со строками
# def get_bin2(n):
#     bin = ""
#     while n > 0:
#         bin = str(n%2) + bin
#         n = n//2
#     return bin

n = int(input('Введите десятичное число, которое хотите перевести в двоичное: '))

# print(f'Число {n} в двоичной системе исчисления равно {get_bin2(n)}')
print(f'Число {n} в двоичной системе исчисления равно: ')
get_bin(n)
