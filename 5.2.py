with open('5_2.txt') as f:
    line_count = 0
    for line in f:
        line_count += 1

        list = 0
        word = 0
        for j in line:
            if j != ' ' and list == 0:
                word += 1
                list = 1
            elif j == ' ':
                list = 0

        print(line, word, 'сл.')

    print("Количество строк в файле: ", line_count)
    f.close()
