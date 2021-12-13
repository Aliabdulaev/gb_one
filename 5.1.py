with open('file_1.txt', 'w') as f:
    while True:
        line = input('Введите новую строку - ')
        if not line:
            break
    f.write(line + '\n')
f.close()

