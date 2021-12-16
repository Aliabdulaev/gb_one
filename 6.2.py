class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width


    def mass(self):
        return f"{self._length} м * {self._width} м * 25 кг * 5 см = {(self._length * self._width * 25 * 5) / 1000} т"

r = Road(20, 5000)
print(r.mass())
