mylist = {}
with open("5_6.txt") as f:
    for line in f:
        name, stats = line.split(':')
        el = [i for i in stats if i == ' ' or (i >= '0' and i <= '9')]
        print(el)
        name_sum = sum(map(int,"".join(el).split()))
        mylist[name] = name_sum
print(f"{mylist}")


