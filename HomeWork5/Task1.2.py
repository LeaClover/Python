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
