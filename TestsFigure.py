import unittest
from Figures import Circle, Triangle
from math import pi


class TestFigures(unittest.TestCase):
    def setUp(self):
        self.triangle = Triangle(3, 4, 5)
        self.circle = Circle(1)

    def test_triangle_square(self):
        self.assertTrue(self.triangle.square == 6.0)

    def test_circle_square(self):
        self.assertEqual(self.circle.square, pi)