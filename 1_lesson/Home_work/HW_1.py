# 1. Найдите сумму цифр трехзначного числа.

n = int(input("Введите число: \n"))
m = 0
while n != 0:
    m = m + n % 10
    n = n // 10
print(m)
