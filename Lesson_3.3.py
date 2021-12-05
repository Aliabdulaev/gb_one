def my_func(arg_1: int, arg_2: int, arg_3: int) -> int:
    my_list = [arg_1, arg_2, arg_3]
    try:
        my_list.remove(min(my_list))
        return sum(my_list)
    except TypeError:
        return "Выбери только число"

print(my_func(5, 8, 55))

