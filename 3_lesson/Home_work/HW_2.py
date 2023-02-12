# Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное
# число N – количество элементов в массиве. В последующих строках
# записаны N целых чисел Ai. Последняя строка содержит число X

len_mas = int(input("Введите кол-во элементов в массиве: \n"))
print(list(i for i in range(len_mas)))
search_num = int(input("Введите искомое число: \n"))
answer = 0
massiv = [i for i in range(len_mas)]
for i in range(len_mas):
    if massiv[i] == search_num:
        answer = massiv[i]
    elif massiv[0] > search_num:
        answer = massiv[0]
    else:
        answer = massiv [len_mas -1]
print(answer)
