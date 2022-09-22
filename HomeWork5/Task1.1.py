# На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

import random
logs = open('CandiesLogs1.txt', 'a')

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
        if first > max_grap or first < 0:
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
        second = int(input('Второй игрок: '))
        logs.write(f'Second player: {first}\n')
        if second > max_grap or second < 0:
            while second > max_grap or second < 0:
                print('Введенно неверное значение! Повторите попытку')
                logs.write('Incorrect value! Please, try again!\n')
                second = int(input('Второй игрок: '))
                logs.write(f'Second player: {first}\n')
        candies = candies - second
        count2 = count2 + second
        print(f'Осталось {candies} конфет')
        logs.write(f'{candies} candies left!\n')
        turn = 0
if candies == 0 and turn == 0:
    print(f'Победил второй игрок!!! Итого он собрал {count2} конфет для победы!')
    logs.write(f'The second player win!!! Collect {count2} candies!\n')
elif candies == 0 and turn == 1:
    print(f'Победил первый игрок!!! Итого он собрал {count1} конфет для победы!')
    logs.write(f'The first player win!!! Collect {count2} candies!\n')
logs.close()
