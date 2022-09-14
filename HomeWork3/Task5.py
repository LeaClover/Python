# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def fibonachi(n):
    if n==1 or n ==2:
        return 1
    else:
        return fibonachi(n-1) + fibonachi(n-2)

def nega_fib(n):
    if n>0:
        return fibonachi(n)
    elif n==0:
        return(0)
    else:
        sign = int((-1)**(n+1))
        num = fibonachi(-n)
        return sign*num

def print_negafib(n):
    negafib = list()
    i = 0
    while i <= n:
        negafib.append(nega_fib(-i))
        i = i + 1
    negafib.reverse()
    fib = list()
    i = 1
    while i <= n:
        fib.append(nega_fib(i))
        i = i + 1
    full_fib = []
    for i in range(n+1):
        full_fib.append(negafib[i])
    for i in range(n):
        full_fib.append(fib[i])
    print(full_fib)

n = int(input('Введите количество чисел НегаФибоначчи, которое надо вывести: '))
print('Последовательность НегаФибоначчи: ')
print_negafib(n)
