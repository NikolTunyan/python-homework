# Базовый класс для Фигуры
class Figure:
    def area(self):
        pass

    def volume(self):
        pass

# 2D фигуры
class TwoDimensionalFigure(Figure):
    def area(self):
        pass

# 3D фигуры
class ThreeDimensionalFigure(Figure):
    def volume(self):
        pass

# Квадрат (2D фигура)
class Square(TwoDimensionalFigure):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        # Формула для площади квадрата: a * a
        return self.side_length ** 2

# Треугольник (2D фигура)
class Triangle(TwoDimensionalFigure):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        # Формула для площади треугольника: (0.5 * b * h)
        return 0.5 * self.base * self.height

    @staticmethod
    def area_from_side_and_two_angles(side, angle1, angle2):
        # Формула для площади треугольника по длине стороны и двум углам: (0.5 * a^2 * sin(B) * sin(C) / sin(A))
        import math
        angle3 = 180 - angle1 - angle2
        return 0.5 * side**2 * math.sin(math.radians(angle1)) * math.sin(math.radians(angle2)) / math.sin(math.radians(angle3))

    @staticmethod
    def area_from_three_sides(side1, side2, side3):
        # Формула для площади треугольника по трем сторонам: sqrt(s * (s - a) * (s - b) * (s - c)), где s - полупериметр
        s = (side1 + side2 + side3) / 2
        return (s * (s - side1) * (s - side2) * (s - side3))**0.5

# Куб (3D фигура)
class Cube(ThreeDimensionalFigure):
    def __init__(self, side_length):
        self.side_length = side_length

    def volume(self):
        # Формула для объема куба: a * a * a
        return self.side_length ** 3

# Конус (3D фигура)
class Cone(ThreeDimensionalFigure):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        # Формула для объема конуса: (1/3) * pi * r^2 * h
        return (1/3) * 3.14159 * self.radius**2 * self.height

# Функция для выбора формулы для вычисления площади треугольника
def choose_triangle_formula():
    print("Выберите формулу для вычисления площади треугольника:")
    print("1. Исходя из длины стороны и двух углов")
    print("2. Исходя из длин трех сторон")
    choice = input("Введите номер выбранной формулы (1 или 2): ")
    return choice

# Пример использования
square = Square(5)
triangle = Triangle(4, 3)
cube = Cube(3)
cone = Cone(2, 4)

print(f"Площадь квадрата: ({square.side_length} * {square.side_length}) = {square.area()}")
print(f"Площадь треугольника: (0.5 * {triangle.base} * {triangle.height}) = {triangle.area()}")

# Выбор формулы для площади треугольника
triangle_formula_choice = choose_triangle_formula()

if triangle_formula_choice == '1':
    side = float(input("Введите длину стороны треугольника: "))
    angle1 = float(input("Введите угол A: "))
    angle2 = float(input("Введите угол B: "))
    print(f"Площадь треугольника: {Triangle.area_from_side_and_two_angles(side, angle1, angle2)}")
elif triangle_formula_choice == '2':
    side1 = float(input("Введите длину стороны a: "))
    side2 = float(input("Введите длину стороны b: "))
    side3 = float(input("Введите длину стороны c: "))
    print(f"Площадь треугольника: {Triangle.area_from_three_sides(side1, side2, side3)}")
else:
    print("Неверный выбор формулы.")
