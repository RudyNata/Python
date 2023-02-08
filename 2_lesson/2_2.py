# Дано натуральное число A > 1. Определите, каким по счету числом
# Фибоначчи оно является, то есть выведите такое числоn, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.

num = int(input("Введите число: \n"))
count = 2
n1 = 0
n2 = 1
while n2 <= num:
    if n2 == num:
        print(f"{count} по счету число Фибоначчи")
        break
    n1, n2 = n2, n1 + n2
    count += 1
else:
    print(-1)