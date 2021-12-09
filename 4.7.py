from math import factorial

def factorial_gen(n):
    for i in range(n):
        print(i, end='! = ')
        yield factorial(i)

print("<<Вычисления факториала числа>>")
for el in factorial_gen(10):
    print(el)