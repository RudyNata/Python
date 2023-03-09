# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.

# def print_operation_table(operation, num_rows=6, num_columns=6):
#     for i in range(1, num_columns+1):
#         for j in range(1, num_rows+1):
            # print(lambda i, j: i * j)

# operations = lambda x, y: x * y
def print_operation_table(operation, num_rows, num_columns):
    for i in range(1, num_columns+1):
        print('')
        print(i, end =" ")
        for j in range(1, num_rows +1):
            print(i*j, end =" ")
    print('')
    column = int(input('Введите номер столбца: '))
    row = int(input('Введите номер строки: '))
    print(operation(column, row))

print_operation_table(lambda x, y: x * y, 6, 6)