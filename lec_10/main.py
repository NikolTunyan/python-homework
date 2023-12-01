class Vehicle:
    def __init__(self):
        print('Base class')


class Car(Vehicle):
    def __init__(self):
        super().__init__()
        print('Car class')


class Plane(Vehicle):
    def __init__(self):
        super().__init__()
        print('Plane class')


class Boat(Vehicle):
    def __init__(self):
        super().__init__()
        print('Boat class')


class RaceCar(Car):
    def __init__(self):
        super().__init__()
        print('RaceCar class')


if __name__ == "__main__":
    vehicle = Vehicle()
    car = Car()
    plane = Plane()
    boat = Boat()
    race_car = RaceCar()
