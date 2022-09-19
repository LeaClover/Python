# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

def list_of_prime_factors(n):
    i = 2
    prime_factors = list()
    while i <= n:
        if n%2 == 0:
            prime_factors.append(i)
            n = n / i
            i = 1
        elif n%2 == 1 and n%i == 0:
            prime_factors.append(i)
            n = n / i
            i = 1
        i += 1
    print(prime_factors)

n = int(input('Введите число для составления списка его простых множителей: '))
list_of_prime_factors(n)
