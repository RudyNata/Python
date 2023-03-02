# Напишите программу, которая на вход принимает два числа
# A и B, и возводит число А в целую степень B с помощью рекурсии.

def step(a, b):
    if b == 0:
        return 1
    return a * step(a, b -1)

print(step(int(input()), int(input())))
