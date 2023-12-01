class Fraction:
  def __init__(self, numerator, denominator):
      # Проверяем, что знаменатель не равен нулю
      if denominator == 0:
          raise ValueError("Знаменатель не может быть равен нулю.")

      self.numerator = numerator
      self.denominator = denominator
      self.simplify()  # Упрощаем дробь при инициализации

  def simplify(self):
      # Находим наибольший общий делитель и используем его для упрощения дроби
      common = self.find_common_divisor(self.numerator, self.denominator)
      self.numerator //= common
      self.denominator //= common

  def find_common_divisor(self, a, b):
      # Находим наибольший общий делитель двух чисел
      while b:
          a, b = b, a % b
      return a

  def __str__(self):
      return f"{self.numerator}/{self.denominator}"

  def __add__(self, other):
      # Сложение дробей
      new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
      new_denominator = self.denominator * other.denominator
      return Fraction(new_numerator, new_denominator)

  def __sub__(self, other):
      # Вычитание дробей
      new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
      new_denominator = self.denominator * other.denominator
      return Fraction(new_numerator, new_denominator)

  def __mul__(self, other):
      # Умножение дробей
      new_numerator = self.numerator * other.numerator
      new_denominator = self.denominator * other.denominator
      return Fraction(new_numerator, new_denominator)

  def __truediv__(self, other):
      # Деление дробей
      if other.numerator == 0:
          raise ValueError("Нельзя делить на ноль.")

      new_numerator = self.numerator * other.denominator
      new_denominator = self.denominator * other.numerator
      return Fraction(new_numerator, new_denominator)

# Пример использования
fraction1 = Fraction(1, 1235)
fraction2 = Fraction(1, 1235)

print("Дробь 1:", fraction1)
print("Дробь 2:", fraction2)

sum_fraction = fraction1 + fraction2
print("Сумма:", sum_fraction)

difference_fraction = fraction1 - fraction2
print("Разность:", difference_fraction)

product_fraction = fraction1 * fraction2
print("Произведение:", product_fraction)

quotient_fraction = fraction1 / fraction2
print("Частное:", quotient_fraction)
