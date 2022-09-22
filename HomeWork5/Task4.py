# Шифр Юлия Цезаря

def cip(word, n, al):
    arr_index = list()
    i = 0
    j = 0
    while i < len(word):
        while j < len(al):
            if al[j] == word[i]:
                arr_index.append(j)
            j += 1
        j = 0
        i += 1
    print(arr_index)
    new_index = list()
    for el in range(len(arr_index)):
        if arr_index[el] + n >= len(al):
            new_index.append(n - ((len(al)-1) - arr_index[el]) - 1)
        else:
            new_index.append(arr_index[el] + n)
    print(new_index)
    new_word = ''
    i = 0
    while i < len(word):
        new_word = new_word + al[new_index[i]]
        i += 1
    print(new_word)

al = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 
    'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

word = input('Введите строку заглавными буквами на латинице без пробелов: ')
n = int(input('Введите шаг: '))
cip(word, n, al)
