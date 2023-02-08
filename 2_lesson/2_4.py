# Пользователь вводит одно число N – количество арбузов.
# Вторая строка содержит N чисел, записанных на новой строчке
# каждое. Здесь каждое число – это масса соответствующего
# арбуза. Найти меньшее и большее. 5 -> 5 1 6 5 9, Output: 1 9

qty_watermelon = int(input("Введите кол-во арбузов: \n"))
max_weight = 0
min_weight = 100
for i in range(qty_watermelon):
    weight = int(input())
    if weight > max_weight:
        max_weight = weight
    elif weight < min_weight:
        min_weight = weight
print(f"Самы тяжелый арбуз весом {max_weight}, самый лёгкий арбуз весом {min_weight}")