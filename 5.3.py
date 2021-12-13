with open('5_3.txt', 'r') as f:
    lst = list()
    for line in f.readlines():
        lst.extend(line.rstrip().split(' '))
print(lst)

print("\nОклад меньше 20000 у сотрудников: ")
summ = 0
for i in range(1, len(lst), 2):
    a = int(lst[i])
    summ += a
    count = len(lst) / 2
    if a <= 20000:
        print(lst[i-1])
middle_profit = summ / count
print("\nСредняя величина дохода сотрудников: ", "%.1f" % middle_profit)
