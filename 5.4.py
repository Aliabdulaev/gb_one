
with open('5_4.txt', 'r') as f:
    lst = list()
    for line in f.readlines():
        lst.extend(line.split(' '))
print(lst)

rus_lst = ["Один", "Два", "Три", "Четыре"]

j = 0
for i in range(0, len(lst), 3):
    lst[i] = rus_lst[j]
    j += 1

print(lst)
out_f = open('5_4rus.txt', 'w')
out_f.writelines(lst)
out_f.close()