# 3. Напишите программу, которая определит позицию второго вхождения
#  строки в списке либо сообщит, что её нет.
# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

a = list()
for i in range(5):
    a.append(input())
print(a)

b = input('Введите строку для проверки: ')

count = 0
for i in a:
    if i == b:
        count += 1
if count == 0:
    print('no')
else:
    print(count)

# Второе решение
# list_1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# string = input('введите строку: ')
# count = 0
# i = 0
# flag = True
# while i < len(list_1) and flag:
#     if string == list_1[i]:
#         count += 1
#         if count == 2:
#             flag = False
#             print(i)
#     i += 1
    
# if flag:
#     print(-1)


