# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n

# Длинное решение:
# string = input().split()

# for i in range(len(string)):
#     count = 1
#     for j in range(i + 1, len(string)):
#         if string[i] == string[j]:
#             string[j] += "_" + str(count)
#             count += 1

# print(*string)

# Корректно:

string = input().split()
D = {}.fromkeys(string, 0)

for i in string:
    print(f"{i}_{D[i]}" if D[i] else i, end=" ")
    D[i] += 1