
class Cell:
    def __init__(self, num_c):
        self.num_c = num_c        # количество клеток quantity cell

    def __add__(self, other):
        return self.num_c + other

    def __sub__(self, other):
        return self.num_c - other

    def __mul__(self, other):
        return self.num_c * other

    def __truediv__(self, other):
        return round(self.num_c / other)

    def make_cell(self, cell_in_row):       # количество клеток в ряду
        self.cell_fall = ""
        while self.num_c > 0:
            self.num_c -= cell_in_row
            if self.num_c < 0:
                self.cell_fall += ("*" * (cell_in_row + self.num_c) + "\n")
            else:
                self.cell_fall += ("*" * cell_in_row + "\n")
        return self.cell_fall

    def __call__(self, new_num_c):
        self.num_c = new_num_c


c = Cell(52)                # введите количество клеток
print(c.make_cell(10))      # количество клеток в ряду
print(c+15)
c(99)
print(c.num_c)
print(c/2)