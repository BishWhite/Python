import unittest
from math import sqrt


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):         # zwraca string "(x, y)"
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):        # zwraca string "Point(x, y)"
        return "Point({}, {})".format(self.x, self.y)

    def __eq__(self, other):   # obsługa point1 == point2
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __sub__(self, other):  # v1 - v2
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        
        return self.x * other.y - self.y * other.x

    def length(self):
        
        return sqrt(self.x ** 2 + self.y ** 2)


# Kod testujący moduł.
class TestPoint(unittest.TestCase):

    def setUp(self):
        pass

    def test___str__(self):
        self.assertEqual(str(Point(1, 5)), '(1, 5)')
        self.assertEqual(str(Point(0, 3)), '(0, 3)')

    def test___repr__(self):
        self.assertEqual(repr(Point(1, 5)), 'Point(1, 5)')
        self.assertEqual(repr(Point(0, 3)), 'Point(0, 3)')

    def test___eq__(self):
        self.assertEqual(Point(1, 7), Point(1, 7))
        self.assertEqual(Point(1, 0), Point(1, 0))

    def test___ne__(self):
        self.assertNotEqual(Point(1, 2), Point(0, -3))
        self.assertNotEqual(Point(2, 0), Point(-7, 1))

    def test___add__(self):
        self.assertEqual(Point(1, 2) + Point(4, 4), Point(5, 6))
        self.assertEqual(Point(-1, 2) + Point(2, 3), Point(1, 5))

    def test___sub__(self):
        self.assertEqual(Point(3, 2) - Point(3, 4), Point(0, -2))
        self.assertEqual(Point(-1, 4) - Point(2, 3), Point(-3, 1))

    def test___mul__(self):
        self.assertEqual(Point(1, 2) * Point(3, 4), 11)
        self.assertEqual(Point(-8, 4) * Point(2, 3), -4)

    def test_cross(self):
        self.assertEqual(Point(1, 2).cross(Point(3, 4)), -2)
        self.assertEqual(Point(-8, 4).cross(Point(2, 3)), -32)

    def test_length(self):
        self.assertEqual(Point(-5, 0).length(), 5)
        self.assertEqual(Point(2, 4).length(), sqrt(20))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()