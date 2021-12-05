def div(num_1, num_2):

    try:
        num_1 = int(num_1)
        num_2 = int(num_2)
        div_num = num_1 / num_2
    except ValueError:
        return'Некорректные данные'
    except ZeroDivisionError:
        return 'На ноль делить нельзя'
    return round(div_num, 3)

print(div(input('Введите число №1 - '), input('Введите число №2 - ')))

