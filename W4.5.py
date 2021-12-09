from functools import reduce

my_list = [i for i in range(100, 1001, 2)]
print("Список чётных чисел в диапазоне [100..1000]:\n", my_list)
print("Произведение всех элементов списка:\n", reduce(lambda x,y: x*y, my_list))