from datetime import datetime

def print_result(result, number_first, number_second, answer):
    with open('result.txt', 'a+', encoding='UTF-8') as file:
        file.write(f'{number_first} {answer} {number_second} = {result} --- {datetime.now()}\n')
        