"""Реализовать базовый класс Worker (работник), в котором определить атрибуты: name,
surname, position (должность), income (доход). Последний атрибут должен быть
защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"profit": profit, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учетом премии (get_full_profit). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов,
вызвать методы экземпляров)."""


class Worker:
    # атрибуты класса
    def __init__(self, name, surname, position, wage, bonus  ):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"Оклад": wage, "Премия": bonus}

class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_full_profit(self):
        return f"{sum(self._income.values())}"

engineer = Position("Ali", 'Abdulaev', "supervisor", 80000, 40000)

print(engineer.get_full_name())
print(engineer.position)
print(engineer.get_full_profit())

