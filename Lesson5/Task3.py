# Напишите программу, удаляющую из текста все слова, содержащие "абв".

stroka = 'ПривабВет, каабв твои дела? Чем сегоабв занят?'
print(' '.join(list(filter(lambda x: 'абв' not in x.lower(), stroka.split()))))


# stroka = 'ПривабВет, каабвк твои дела? Чем сегоабв занят?'
# stroka1 = stroka.lower().replace('абв', '')
# print(stroka1)