class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f"Новая машина: {self.name} (Цвет {self.color}) Полицейская машина - {self.is_police}")

    def go(self):
        print(f"{self.name}: Машина поехала")

    def stop(self):
        print(f"{self.name}: Машина остановилась")

    def turn(self, direction):
        print(f"{self.name}: Машина повернула {'налево' if direction == 0 else 'направо'}")

    def full_info(self):
        print(f"{self.name}: Скорость автомобиля - {self.speed}")

class WorkCar(Car):
    def full_info(self):
        return f"{self.name}: Скороть автомобиля - {self.speed} - ВНИМАНИЕ Превышение скорости !" \
            if self.speed > 49 else f"{self.name}: Скорость автомобиля - {self.speed}"

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


police_car = PoliceCar("Bugatti", "White", 300, True)
police_car.go()

