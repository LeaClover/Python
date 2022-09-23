# Создайте программу для игры в ""Крестики-нолики"".

import random
logs = open('TicTacToeLogs.txt', 'a')

matrix = [['*', '*', '*'], ['*','*','*'], ['*', '*', '*']]

for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        print(matrix[i][j], end=' ')
        if j == 2:
            logs.write(f'{matrix[i][j]}\n')
        else:
            logs.write(f'{matrix[i][j]} ')
    print()

turn = int(random.randint(0, 1))
if turn == 0:
    print('Первым ходит первый игрок! --> O')
    logs.write('First player turn! --> O\n')
elif turn == 1:
    print('Первым ходит второй игрок! --> X')
    logs.write('Second player turn! --> X\n')
print('Введите 2 числа координат через пробел от 1 до 3.')
logs.write('Enter 2 numbers using a "space" button (for 1 to 3).\n')

for i in range(0, len(matrix)): 
    for j in range(0, len(matrix[i])):
        if ((matrix[0][0] == 'O' and matrix[0][1] == 'O' and matrix[0][2] == 'O') or 
            (matrix[1][0] == 'O' and matrix[1][1] == 'O' and matrix[1][2] == 'O') or
            (matrix[2][0] == 'O' and matrix[2][1] == 'O' and matrix[2][2] == 'O') or
            (matrix[0][0] == 'O' and matrix[1][0] == 'O' and matrix[2][0] == 'O') or
            (matrix[0][1] == 'O' and matrix[1][1] == 'O' and matrix[2][1] == 'O') or
            (matrix[0][2] == 'O' and matrix[1][2] == 'O' and matrix[2][2] == 'O') or
            (matrix[0][0] == 'O' and matrix[1][1] == 'O' and matrix[2][2] == 'O') or
            (matrix[0][2] == 'O' and matrix[1][1] == 'O' and matrix[2][0] == 'O')):
            print('Выиграл первый игрок!!!')
            logs.write('First player win!\n')
            break
        elif ((matrix[0][0] == 'X' and matrix[0][1] == 'X' and matrix[0][2] == 'X') or 
            (matrix[1][0] == 'X' and matrix[1][1] == 'X' and matrix[1][2] == 'X') or
            (matrix[2][0] == 'X' and matrix[2][1] == 'X' and matrix[2][2] == 'X') or
            (matrix[0][0] == 'X' and matrix[1][0] == 'X' and matrix[2][0] == 'X') or
            (matrix[0][1] == 'X' and matrix[1][1] == 'X' and matrix[2][1] == 'X') or
            (matrix[0][2] == 'X' and matrix[1][2] == 'X' and matrix[2][2] == 'X') or
            (matrix[0][0] == 'X' and matrix[1][1] == 'X' and matrix[2][2] == 'X') or
            (matrix[0][2] == 'X' and matrix[1][1] == 'X' and matrix[2][0] == 'X')):
            print('Выиграл второй игрок!!!')
            logs.write('Second player win!\n')
            break
        else:
            if turn == 0:
                print('Ход первого игрока! --> O')
                logs.write('First player turn! --> O\n')
                first = input().split(' ')
                logs.write(f'{first}\n')
                if (matrix[int(first[0])-1][int(first[1])-1] == 'O' or
                    matrix[int(first[0])-1][int(first[1])-1] == 'X'):
                    while (matrix[int(first[0])-1][int(first[1])-1] == 'O' 
                        or matrix[int(first[0])-1][int(first[1])-1] == 'X'):
                        print('Это поле уже занято! Попробуйте снова!')
                        logs.write('Incorrect! This field is not empty!')
                        first = input().split(' ')
                        logs.write(f'{first}\n')
                matrix[int(first[0])-1][int(first[1])-1] = 'O'
                for i in range(0, len(matrix)):
                    for j in range(0, len(matrix[i])):
                        print(matrix[i][j], end=' ')
                        if j == 2:
                            logs.write(f'{matrix[i][j]}\n')
                        else:
                            logs.write(f'{matrix[i][j]} ')
                    print()
                turn = 1
                i = j = 0
            elif turn == 1:
                print('Ход второго игрока! --> X')
                logs.write('Second player turn! --> X\n')
                second = input().split(' ')
                logs.write(f'{second}\n')
                if (matrix[int(second[0])-1][int(second[1])-1] == 'O' or
                    matrix[int(second[0])-1][int(second[1])-1] == 'X'):
                    while (matrix[int(second[0])-1][int(second[1])-1] == 'O' 
                        or matrix[int(second[0])-1][int(second[1])-1] == 'X'):
                        print('Это поле уже занято! Попробуйте снова!')
                        logs.write('Incorrect! This field is not empty!')
                        second = input().split(' ')
                        logs.write(f'{second}\n')
                matrix[int(second[0])-1][int(second[1])-1] = 'X'
                for i in range(0, len(matrix)):
                    for j in range(0, len(matrix[i])):
                        print(matrix[i][j], end=' ')
                        if j == 2:
                            logs.write(f'{matrix[i][j]}\n')
                        else:
                            logs.write(f'{matrix[i][j]} ')
                    print()
                turn = 0
                i = j = 0
logs.close()

# Второй вариант
# # 2(Кретиски-нолики)

# def input_position():
#     row = int(input('Введите номер строки(1-3): '))
#     while row < 1 or row > 3:
#         row = int(input('Введите номер строки(1-3): '))

#     columns = int(input('Введите номер стобца(1-3): '))
#     while columns < 1 or columns > 3:
#         columns = int(input('Введите номер строки(1-3): ')) 
    
#     return row, columns


# def check(array):
#     if array[0][0] == array[1][0] == array[2][0] != '*':
#         return f'Выиграл {array[0][0]}'
#     elif array[0][1] == array[1][1] == array[2][1] != '*':
#         return f'Выиграл {array[0][1]}'
#     elif array[0][2] == array[1][2] == array[2][2] != '*':
#         return f'Выиграл {array[0][2]}'
#     elif array[0][0] == array[0][1] == array[0][2] != '*':
#         return f'Выиграл {array[0][0]}'
#     elif array[1][0] == array[1][1] == array[1][2] != '*':
#         return f'Выиграл {array[1][0]}'
#     elif array[2][0] == array[2][1] == array[2][2] != '*':
#         return f'Выиграл {array[2][0]}'
#     elif array[0][0] == array[1][1] == array[2][2] != '*':
#         return f'Выиграл {array[0][0]}'
#     elif array[0][2] == array[1][1] == array[2][0] != '*':
#         return f'Выиграл {array[2][0]}'
#     return None


# array = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]

# value = 'X'
# i = 0
# flag = True
# while i < 9 and flag:
#     print('\n'.join(['\t'.join(i) for i in array]))
#     if i % 2 == 0:
#         print('Сейчас ходят крестики')
#         value = 'X'
#     else:
#         print('Сейчас ходят нолики')
#         value = '0'
#     row, columns = input_position()

#     if array[row - 1][columns - 1] != '*':
#         print('Эта позиция занята')
#         row, columns = input_position()
    
#     array[row - 1][columns - 1] = value
#     result = check(array)
#     if result:
#         print(result)
#         flag = False
    
#     i += 1
