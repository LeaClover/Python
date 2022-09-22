# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def comp(s):
    count = 1
    a = ''
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
        elif s[i] != s[i+1]:
            a = a + str(count) + s[i]
            count = 1
    a = a + str(count) + s[i+1]
    return a

def rec(a):
    num = list()
    let = list()
    i = 0
    while i < len(a):
        if i%2 == 0:
            num.append(int(a[i]))
            i += 1
        else:
            let.append(a[i])
            i += 1  
    rec = ''
    for i in range(len(num)):
        rec = rec + let[i]*num[i]
    return rec   

s = input('Введите строку для сжатия: ')
a = comp(s)
print(f'Сжатие: {a}')
b = rec(a)
print(f'Восстановление: {b}')

logs = open('RLE.txt', 'a')
logs.write(f'Please enter: {s}\n')
logs.write(f'Compression: {a}\n')
logs.write(f'Recovery: {b}\n')
logs.close()
