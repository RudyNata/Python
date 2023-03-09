# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться
# в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит
# написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке


stih = input("Введите стих: ").split()
dict_stih = {'аАоОиИыЫуУэЭ': 1}
print (stih)
new = set()
for i in stih:
   new.add(sum([j[1] for j in dict_stih.items() for k in i if k in j[0]]))
print(new)
if len(new) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')


# sum_glas = 0
# for i in stih:
#     print(sum([j[1] for j in dict_stih.items() for k in i if k in j[0]]))
# if sum_glas % len(stih) == 0:
#     print('Парам пам-пам')
# else:
#     print('Пам парам')



# sum([i[1] for i in el.items() for j in stih if j in i[0]])

# def same_by(characteristic, objects):
#     return len(set(map(characteristic, objects))) == 1

# if same_by(sum([j[1] for j in dict_stih.items() for k in stih if k in j[0]]), stih):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')

