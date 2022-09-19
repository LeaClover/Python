# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

def unique_numbers(str):
    str = str.split(sep=' ')
    numbers = []
    for i in str:
        numbers.append(int(i))
    for i in numbers:
        index = 0
        count = 0
        while index < len(numbers):
            if i == numbers[index]:
                count += 1
                if count > 1:
                    numbers.remove(numbers[index])
                    count = 1
            index += 1
    print(numbers)

str_numbers = input('Введите последовательность чисел через пробел: ')
print('Cписок неповторяющихся элементов исходной последовательности: ')
unique_numbers(str_numbers)
