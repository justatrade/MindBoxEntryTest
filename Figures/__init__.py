from math import pi
from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, r):
        self.r = abs(r)

    @abstractmethod
    def square(self):
        raise NotImplementedError("Not available for abstract class")


class Circle(Figure):
    def __init__(self, r: float):
        super().__init__(r)

    @property
    def square(self) -> float:
        return pi * self.r ** 2


class Triangle(Figure):
    def __init__(self, r: float, *args):
        super().__init__(r)
        if args and len(args) == 2:
            b = abs(args[0])
            c = abs(args[1])
            if (self.r + b > c and
                    self.r + c > b and
                    b + c > self.r):
                self.b = abs(args[0])
                self.c = abs(args[1])
            else:
                raise ValueError('Impossible triangle')
        else:
            self.b = self.r
            self.c = self.r
        self.right_angled = self.check_right_angled()

    def check_right_angled(self) -> bool:
        """
        Проверка, является ли треугольник прямоугольным. По теореме Пифагора.
        Гипотенуза ^ 2 = катет1 ^ 2 + катет2 ^ 2
        Чтобы не вычислять другие стороны, сравниваем два квадрата
        максимальной стороны с суммой квадратов всех сторон
        :return: Возвращает True, ести треугольник прямоугольный, иначе False
        """
        max_size_square = max(self.r, self.b, self.c) ** 2
        all_sizes_square_sum = (self.r ** 2 + self.b ** 2 + self.c ** 2)
        return max_size_square * 2 == all_sizes_square_sum

    @property
    def perimeter(self):
        return self.r + self.b + self.c

    @property
    def square(self):
        p = self.perimeter / 2
        return (p * (p - self.r) * (p - self.b) * (p - self.c)) ** 0.5
