"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
__init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде
прямоугольной схемы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д."""

a = [[31, 37, 51], [22, 43, 86], [3, 5, 8]]
b = [[3, 5, -1], [-5, 4, 64], [32, 6, -8]]

class Matrix:
    def __init__(self, list_of_lists):
        self.list = list_of_lists

    def __str__(self):
        string = ''
        for i in self.list:
            for j in i:
                string = string + '%s\t' % (j)
            string = string[:-1]
            string = string + '\n'
        string = string[:-1]
        return string

    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.list)):
            for j in range(len(self.list[0])):
                summa = other.list[i][j] + self.list[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.list[0]):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


mtrx_1 = Matrix(a)
mtrx_2 = Matrix(b)

print("\nМатрица №1")
print(mtrx_1.__str__(), "\n")

print("Матрица №2")
print(mtrx_2.__str__(), "\n")

print("Сумма матриц №1 и №2")
print(mtrx_1 + mtrx_2)