import unittest
from points import Point


class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        # Chcemy, aby x1 < x2, y1 < y2.
        if not x1 < x2:
            raise ValueError('x1 > x2')
        if not y1 < y2:
            raise ValueError('y1 > y2')

        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):         # "[(x1, y1), (x2, y2)]"
        return "[{}, {}]".format(self.pt1, self.pt2)

    def __repr__(self):        # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle({}, {}, {}, {})".format(
            self.pt1.x, self.pt1.y,
            self.pt2.x, self.pt2.y)

    def __eq__(self, other):   # obsługa rect1 == rect2
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):          # zwraca środek prostokąta
        
        x = (self.pt1.x + self.pt2.x) / 2
        y = (self.pt1.y + self.pt2.y) / 2
        return Point(x, y)

    def area(self):            # pole powierzchni
        
        width = abs(self.pt1.x) + abs(self.pt2.x)
        length = abs(self.pt1.y) + abs(self.pt2.y)
        return width * length

    def move(self, x, y):      # przesunięcie o (x, y)

        vector = Point(x, y)
        self.pt1 += vector
        self.pt2 += vector
        return self

    def intersection(self, other):  # część wspólna prostokątów
        x1 = max(self.pt1.x, other.pt1.x)
        y1 = max(self.pt1.y, other.pt1.y)
        x2 = min(self.pt2.x, other.pt2.x)
        y2 = min(self.pt2.y, other.pt2.y)
        try:
            return Rectangle(x1, y1, x2, y2)
        except ValueError:
            raise ArithmeticError('Prostokaty nie mają części wspólnej')

    def cover(self, other):    # prostąkąt nakrywający oba
        x1 = min(self.pt1.x, other.pt1.x)
        y1 = min(self.pt1.y, other.pt1.y)
        x2 = max(self.pt2.x, other.pt2.x)
        y2 = max(self.pt2.y, other.pt2.y)

        return Rectangle(x1, y1, x2, y2)

    def make4(self):           # zwraca listę czterech mniejszych
        
        center = self.center()

        top_right = Rectangle(center.x, center.y, self.pt2.x, self.pt2.y)
        top_left = Rectangle(self.pt1.x, center.y, center.x, self.pt2.y)
        bottom_left = Rectangle(self.pt1.x, self.pt1.y, center.x, center.y)
        bottom_right = Rectangle(center.x, self.pt1.y, self.pt2.x, center.y)

        return (top_right, top_left, bottom_left, bottom_right)

# Kod testujący moduł.


class TestRectangle(unittest.TestCase):

    def setUp(self):
        pass

    def test___init__(self):
        self.assertRaises(ValueError, lambda: Rectangle(7, 0, 1, 3))
        self.assertRaises(ValueError, lambda: Rectangle(0, 5, 3, 1))

    def test___str__(self):
        self.assertEqual(str(Rectangle(0, 1, 1, 4)), '[(0, 1), (1, 4)]')
        self.assertEqual(str(Rectangle(1, 2, 3, 5)), '[(1, 2), (3, 5)]')

    def test___repr__(self):
        self.assertEqual(repr(Rectangle(1, 2, 4, 6)), 'Rectangle(1, 2, 4, 6)')
        self.assertEqual(repr(Rectangle(-1, 4, 3, 5)),'Rectangle(-1, 4, 3, 5)')

    def test___eq__(self):
        self.assertEqual(Rectangle(1, 2, 3, 4), Rectangle(1, 2, 3, 4))
        self.assertEqual(Rectangle(-3, -2, -1, 1), Rectangle(-3, -2, -1, 1))

    def test_center(self):
        self.assertEqual(Rectangle(0, 0, 6, 4).center(), Point(3, 2))
        self.assertEqual(Rectangle(0, 0, 1, 1).center(), Point(0.5, 0.5))

    def test_area(self):
        self.assertEqual(Rectangle(0, 0, 4, 4).area(), 16)
        self.assertEqual(Rectangle(0, 0, 8, 10).area(), 80)

    def test_move(self):
        self.assertEqual(Rectangle(0, 0, 4, 2).move(1, 1), Rectangle(1, 1, 5, 3))
        self.assertEqual(Rectangle(0, 0, 6, 3).move(-1, 2), Rectangle(-1, 2, 5, 5))

    def test_intersection(self):
        self.assertRaises(ArithmeticError, lambda: Rectangle(0, 0, 1, 1).intersection(Rectangle(2, 2, 3, 3)))
        self.assertEqual( Rectangle(0, 0, 4, 4).intersection(Rectangle(0, 0, 4, 4)), Rectangle(0, 0, 4, 4))
        self.assertEqual( Rectangle(0, 0, 4, 4).intersection(Rectangle(3, 2, 4, 3)), Rectangle(3, 2, 4, 3))
        self.assertEqual( Rectangle(0, -2, 4, 2).intersection(Rectangle(-3, 0, 2, 5)), Rectangle(0, 0, 2, 2))
        

    def test_cover(self):
        self.assertEqual( Rectangle(0, 0, 2, 2).cover(Rectangle(0, 0, 2, 2)), Rectangle(0, 0, 2, 2))
        self.assertEqual( Rectangle(0, 0, 4, 4).cover(Rectangle(2, 2, 10, 10)), Rectangle(0, 0, 10, 10))
        self.assertEqual( Rectangle(0, 1, 5, 8).cover(Rectangle(1, 0, 8, 5)), Rectangle(0, 0, 8, 8))

    def test_make4(self):
        top_right = Rectangle(4, 2, 8, 4)
        top_left = Rectangle(0, 2, 4, 4)
        bottom_left = Rectangle(0, 0, 4, 2)
        bottom_right = Rectangle(4, 0, 8, 2)
        rectangles = (top_right, top_left, bottom_left, bottom_right)
        self.assertEqual(Rectangle(0, 0, 8, 4).make4(), rectangles)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()