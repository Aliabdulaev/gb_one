from sys import argv

script_name, time, rate, bonus = argv

print("Имя скрипта: ", script_name)
print("\n<< Программа рассчета заработной платы сотрудника >>")
print("Выработка в часах: ", time)
print("Ставка в час: ", rate)
print("Премия: ", bonus)
print("Зарплата сотрудника: ", (int(time) * int(rate)) + int(bonus))