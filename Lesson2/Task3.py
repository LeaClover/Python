# 3. Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

# НЕ РАБОТАЕТ!!!

text1 = input('Первая строка: ')
text2 = input('Вторая строка: ')
count = 0

for i in text1:
    if i+(i+1) == text2:
        count += 1

print(count)
