# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но
# наоборот: все максимальные – на минимальные.

from random import *

def grade(numbers):
    Min = min(numbers)
    Max = max(numbers)
    return [Min if i == Max else i for i in numbers]

print("Введите оценоки:")
print(*grade([int(i) for i in input().split()])) # list_grade = [randint(1, 5) for _ in range(int(n))]
