from itertools import count

print("<<Бесконечный итератор целых чисел, начиная с указанного>>")
n = int(input("Введите целое число:"))

for i in count(n):
    print(i, end=' ')
    break

from itertools import cycle

list = [5, 3, 3, 1, 0, 4, 2, 4, 7, 3]
for i in cycle(list):
    print(i, end=' ')
    break
    