# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг -
# циклический) на K элементов вправо, K – положительное число.

list_2 = [1, 2, 3, 4, 5]
k = 3
for i in range(k - 1):
    list_2.insert(0, list_2.pop(- 1))
print(list_2)