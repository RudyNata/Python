# Требуется найти N-е число Фибоначчи

def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)

num = int(input("Введите число: \n"))
print(fib(num))