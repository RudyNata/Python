# Требуется вычислить, сколько раз встречается некоторое число X в
# массиве A[1..N]. Пользователь в первой строке вводит натуральное
# число N – количество элементов в массиве. В последующих строках
# записаны N целых чисел Ai. Последняя строка содержит число X

# len_mas = int(input("Введите кол-во элементов в массиве: \n"))
# print(list(i for i in range(len_mas)))
# search_num = int(input("Введите искомое число: \n"))
# print(sum([1 for i in range(len_mas) if list(i for i in range(len_mas))[i] == search_num]))

#Корректное решение:

list_num = [int(input()) for _ in range (int(input("Введите кол-во элементов в массиве: \n")))]
print("Число встречается раз:")
print(list_num.count(int(input("Введите искомое число: \n"))))