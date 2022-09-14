# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора 
# псевдослучайных чисел.

import time

r = []
for i in range(50):
    time.sleep(1)
    r = print(int(time.time()))

# import time
# from random import randint

# arr = list()
# for i in range(10):
#     number = randint(1, 5)
#     time.sleep(1)
#     arr.append(int(str(time.time())[-number:]))
# print(*arr)
