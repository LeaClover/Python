# Игра с конфетами против бота.

import random
logs = open('CandiesLogs2.txt', 'a')

candies = 2021
logs.write(f'Total {candies} candies!\n')
max_grap = 28
count1 = 0
count2 = 0
turn = int(random.randint(0, 1))
while candies > 0:
    if turn == 0:
        first = int(input('Первый игрок: '))
        logs.write(f'First player: {first}\n')
        if first > max_grap or first <= 0:
            while first > max_grap or first < 0:
                print('Введенно неверное значение! Повторите попытку')
                logs.write('Incorrect value! Please, try again!\n')
                first = int(input('Первый игрок: '))
                logs.write(f'First player: {first}\n')
        candies = candies - first
        count1 = count1 + first
        print(f'Осталось {candies} конфет')
        logs.write(f'{candies} candies left!\n')
        turn = 1
    elif turn == 1:
        if max_grap < candies <= max_grap + max_grap + 1 + 1:
            i = candies - (max_grap + 1)
            bot = i
            candies = candies - bot
            count2 = count2 + bot
            print(f'Бот: {bot} конфет')
            logs.write(f'Bot: {bot} candies\n')
            print(f'Осталось {candies} конфет')
            logs.write(f'{candies} candies left!\n')
            turn = 0
        elif max_grap + max_grap + 1 + 1 < candies <= max_grap + max_grap + max_grap + 1:
            i = candies - (max_grap + 1) - (max_grap + 1)
            bot = i
            candies = candies - bot
            count2 = count2 + bot
            print(f'Бот: {bot} конфет')
            logs.write(f'Bot: {bot} candies\n')
            print(f'Осталось {candies} конфет')
            logs.write(f'{candies} candies left!\n')
            turn = 0
        elif 0 < candies <= max_grap:
            bot = candies
            candies = candies - bot
            count2 = count2 + bot
            print(f'Бот: {bot} конфет')
            logs.write(f'Bot: {bot} candies\n')
            print(f'Осталось {candies} конфет')
            logs.write(f'{candies} candies left!\n')
            turn = 0
        else:
            bot = max_grap
            candies = candies - bot
            count2 = count2 + bot
            print(f'Бот: {bot} конфет')
            logs.write(f'Bot: {bot} candies\n')
            print(f'Осталось {candies} конфет')
            logs.write(f'{candies} candies left!\n')
            turn = 0
if candies == 0 and turn == 0:
    print(f'Победил БОТ!!! Итого он собрал {count2} конфет для победы!')
    logs.write(f'The BOT win!!! Collect {count2} candies!\n')
elif candies == 0 and turn == 1:
    print(f'Победил первый игрок!!! Итого он собрал {count1} конфет для победы!')
    logs.write(f'The first player win!!! Collect {count2} candies!\n')
logs.close()


# С ботом второй вариант
# # 1 a
# from random import randint as rd
# from sys import exit


# def check_win(m, n):
#     if m == 1 and n == 0:
#         return 'Выиграл бот'
#     elif m == 0 and n == 0:
#         return 'Выиграл пользователь'
#     return None


# j = 0 # 0 - ходит пользователь, 1 - ход бота
# n = 29
# while n > 0:
#     if n >= 28:
#         count_user = int(input("Сколько Вы хотите взять конфет?(от 1 до 28): "))
#         while count_user < 1 or count_user > 28:
#             count_user = int(input("Вы ошиблись, попробуйте заново\nСколько Вы хотите взять конфет?(от 1 до 28): "))
#     else:
#         count_user = int(input(f"Сколько Вы хотите взять конфет?(от 1 до {n}): "))
#         while count_user < 1 or count_user > n:
#             count_user = int(input(f"Вы ошиблись, попробуйте заново\nСколько Вы хотите взять конфет?(от 1 до {n}): "))
    
#     n = n - count_user
#     print(f'Вы взяли: {count_user}\nОсталось {n} конфет')
#     result = check_win(j, n)
#     if result:
#         print(result)
#         exit()
#     j = 1
#     if n < 28:
#         count_bot = rd(1, n)
#     else:
#         count_bot = rd(1, 28)
#     n = n - count_bot
#     print(f'Бот взял: {count_bot}\nОсталось {n} конфет')
#     result = check_win(j, n)
#     j = 0
#     if result:
#         print(result)
#         exit()

# Умный бот
# # 1 b
# from sys import exit


# def check_win(m, n):
#     if m == 1 and n == 0:
#         return 'Выиграл бот'
#     elif m == 0 and n == 0:
#         return 'Выиграл пользователь'
#     return None


# j = 0 # 0 - ходит пользователь, 1 - ход бота
# n = 60
# while n > 0:
#     if n >= 28:
#         count_user = int(input("Сколько Вы хотите взять конфет?(от 1 до 28): "))
#         while count_user < 1 or count_user > 28:
#             count_user = int(input("Вы ошиблись, попробуйте заново\nСколько Вы хотите взять конфет?(от 1 до 28): "))
#     else:
#         count_user = int(input(f"Сколько Вы хотите взять конфет?(от 1 до {n}): "))
#         while count_user < 1 or count_user > n:
#             count_user = int(input(f"Вы ошиблись, попробуйте заново\nСколько Вы хотите взять конфет?(от 1 до {n}): "))
    
#     n = n - count_user
#     print(f'Вы взяли: {count_user}\nОсталось {n} конфет')
#     result = check_win(j, n)
#     if result:
#         print(result)
#         exit()
#     j = 1
#     count_bot = n % 29 # 0 - бот проиграл
#     if count_bot == 0:
#         count_bot = 1
#     n = n - count_bot
#     print(f'Бот взял: {count_bot}\nОсталось {n} конфет')
#     result = check_win(j, n)
#     j = 0
#     if result:
#         print(result)
#         exit()
