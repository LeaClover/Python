# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной.

import random

def change_coins(coins, n):
    count = 0
    for i in coins:
        if i == 1:
            count += 1
    
    if count <= n/2:
        print(f'Количество монет, которые надо перевернуть: {count}')
    else:
        print(f'Количество монет, которые надо перевернуть: {n-count}')

n = int(input('Введите количество монеток: '))
coins = list(range(1,n+1))

for i in coins:
    coins[i-1] = random.randint(0,1)

print(coins)
change_coins(coins, n)


# Еще 2 варианта решения
# 1)

# n = int(input())
# gerb = 0
# orel = 0
# for i in range(n):
#     k = int(input())
#     if k == 0:
#         gerb += 1
#     else:
#         orel += 1

# print(min(gerb, orel))
# 
# 2)
# n = int(input())
# gerb = 0
# orel = 0
# for i in range(n):
#     k = int(input())
#     if k == 0:
#         gerb += 1
#     else:
#         orel += 1

# if gerb < orel:
#     print(gerb)
# else:
#     print(orel)
