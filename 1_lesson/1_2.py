# В некоторой школе решили набрать три новых математических класса и
# оборудовать кабинеты для них новыми партами. За каждой партой может
# сидеть два учащихся. Известно количество учащихся в каждом из трех
# классов. Выведите наименьшее число парт, которое нужно приобрести для них.

n1 = int(input("Введите кол-во 1 класса: \n"))
n2 = int(input("Введите кол-во 2 класса: \n"))
n3 = int(input("Введите кол-во 3 класса: \n"))
print(-(-(n1+n2+n3)//2))
