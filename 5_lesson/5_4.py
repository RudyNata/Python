# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.

# n = input()
# print(n[::-1])

def revers_el(n):
    if n == 0:
        return ""
    num = input()
    return revers_el(n - 1) + f'{num} '

print(revers_el(int(input())))