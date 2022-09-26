# Таблицы...

def print_operation_table(operation, num_rows = 9, num_columns = 9):
    table = f'\t'
    for num in range(1, num_columns + 1):
        table += f'{num}\t'
    table += f'\n'
    for i in range(1, num_rows + 1):
        table += f'{i}\t'
        for j in range(1, num_columns + 1):
            table += f'{operation(i, j)}\t'
        table += f'\n'
    print(table)
print('Таблица умножения')
print_operation_table(lambda x, y: x * y)
print()
print('Таблица сложения')
print_operation_table(lambda x, y: x + y)
print()
print('Таблица возведения в степень')
print_operation_table(lambda x, y: x**y)


# Еще вариант

# def operation_table(func, row=9, columns=9):
#     for i in range(row):
#         for j in range(columns):
#             print(f'{func(i + 1, j + 1)}', end=' \t')
#         print()


# operation_table(lambda x, y: x * y, 5)
