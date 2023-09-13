import random
import unittest
from Figures import Circle, Triangle
from math import pi


class TestFigures(unittest.TestCase):
    def setUp(self):
        self.a = random.randint(1, 5)
        self.b = random.randint(1, 5)
        self.c = random.randint(20, 100)
        self.triangle = Triangle(3, 4, 5)
        self.circle = Circle(1)

    def test_impossible_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(self.a, self.b, self.c)

    def test_triangle_square(self):
        self.assertTrue(self.triangle.square == 6.0)

    def test_right_angled(self):
        self.assertTrue(self.triangle.right_angled)

    def test_circle_square(self):
        self.assertEqual(self.circle.square, pi)