# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных строках

# def dubl(a):
#     count = 0
#     for i in a:
#         if a.count(i) > 1:
#             count += 1
#     return count//2

# n = int(input("Введите кол-во элементов в массиве А: \n"))
# list_n = [int(input()) for i in range(n)]

# print(dubl(list_n))

mas = [int(input("элементы: ")) for i in range(int(input("кол-во элементов: ")))]
print(mas)
print(sum([mas.count(i) // 2 for i in set(mas)]))