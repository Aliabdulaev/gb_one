from random import randint
with open('5_5.txt', 'w+') as f:
    f.write(" ".join([str(randint(1, 99)) for _ in range(1000)]))
    f.seek(0)
    print(sum(map(int,f.readline().split())))
