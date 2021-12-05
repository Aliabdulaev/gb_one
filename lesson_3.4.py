def my_func(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y>= 0:
            return 'ОШИБКА x должен быть больше нуля, а y должен быть меньше нуля'
        else:
            result = 1
            for _ in range(abs(y)):
                result *= 1/xm
            return f'РЕЗУЛЬТАТ x  в степени y: {round(result, 6)}'
    except ValueError:
        return f'Введите только числа.'

    print(my_func)
    

