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
        return self.side_length ** 2

# Треугольник (2D фигура)
class Triangle(TwoDimensionalFigure):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        # Формула для площади треугольника
        return 0.5 * self.base * self.height

# Куб (3D фигура)
class Cube(ThreeDimensionalFigure):
    def __init__(self, side_length):
        self.side_length = side_length

    def volume(self):
        return self.side_length ** 3

# Конус (3D фигура)
class Cone(ThreeDimensionalFigure):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        # Формула для объема конуса
        return (1/3) * 3.14159 * self.radius**2 * self.height

# Пример использования
square = Square(5)
triangle = Triangle(4, 3)
cube = Cube(3)
cone = Cone(2, 4)

print(f"Площадь квадрата: {square.area()}")
print(f"Площадь треугольника: {triangle.area()}")
print(f"Объем куба: {cube.volume()}")
print(f"Объем конуса: {cone.volume()}")
