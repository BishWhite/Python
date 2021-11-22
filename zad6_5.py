import unittest
from math import gcd


class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y

    def __str__(self):         # zwraca "x/y" lub "x" dla y=1
        if self.y == 1:
            return '{}'.format(self.x)
        return '{}/{}'.format(self.x, self.y)

    def __repr__(self):        # zwraca "Frac(x, y)"
        return "Frac({}, {})".format(self.x, self.y)

    def uprosc(self):
        """Zwraca uproszczony ułamek."""

        x = self.x // gcd(self.x, self.y)
        y = self.y // gcd(self.x, self.y)

        if y < 0:
            x, y = -x, -y

        return Frac(x, y)

    @staticmethod
    def _nww(a, b):
        """Najmniejsza wspólna wielokrotność a i b."""
        return abs(a * b) // gcd(a, b)

    def __add__(self, other):  # frac1 + frac2
        y = Frac._nww(self.y, other.y)
        x = self.x * y // self.y + other.x * y // other.y
        return Frac(x, y).uprosc()

    def __sub__(self, other):  # frac1 - frac2
        y = Frac._nww(self.y, other.y)
        x = self.x * y // self.y - other.x * y // other.y
        return Frac(x, y).uprosc()

    def __mul__(self, other):  # frac1 * frac2
        return Frac(self.x * other.x, self.y * other.y).uprosc()

    def __truediv__(self, other):  # frac1 / frac2
        if other.x == 0:
            raise ZeroDivisionError('Dzielenie przez zero')
        return Frac(self.x * other.y, self.y * other.x).uprosc()

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __lt__(self, other):    	# <
        if float(self) < float(other):
            return True
        return False

    def __gt__(self, other):    	# >
        if float(self) > float(other):
            return True
        return False

    def __le__(self, other):    	# <=
        if float(self) <= float(other):
            return True
        return False

    def __ge__(self, other):    	# >=
        if float(self) >= float(other):
            return True
        return False

    def __eq__(self, other):    	# ==
        if float(self) == float(other):
            return True
        return False

    def __ne__(self, other):            # !=
        if float(self) != float(other):
            return True
        return False

    def __float__(self):       # float(frac)
        return float(self.x) / float(self.y)


class TestFrac(unittest.TestCase):

    def setUp(self):
        pass

    def test___str__(self):
        self.assertEqual(str(Frac(2, 2)), '2/2')
        self.assertEqual(str(Frac(-1, 77)), '-1/77')
        self.assertEqual(str(Frac(-1, -7)), '-1/-7')
        self.assertEqual(str(Frac(1, -4)), '1/-4')
        self.assertEqual(str(Frac(7, 2)), '7/2')
        self.assertNotEqual(str(Frac(1/5)),'1/4')

    def test___repr__(self):
        self.assertEqual(repr(Frac(4, 2)), 'Frac(4, 2)')
        self.assertEqual(repr(Frac(-6, 4)), 'Frac(-6, 4)')
        self.assertEqual(repr(Frac(1, 9)), 'Frac(1, 9)')
        self.assertNotEqual(repr(Frac(4,-2)), 'Frac(-4,2)')

    def test___add__(self):
        self.assertEqual(Frac(1, 3) + Frac(1, 3), Frac(4, 6))
        self.assertEqual(Frac(3, 2) + Frac(6, 4), Frac(3, 1))
        self.assertEqual(Frac(-5,2)+ Frac(7,4), Frac(-3,4))
        self.assertEqual(Frac(-3, 2) + Frac(3, 2), Frac(0, 1))

    def test___sub__(self):
        self.assertEqual(Frac(3, 4) - Frac(3, 4), Frac(0, 2))
        self.assertEqual(Frac(5, 4) - Frac(1, 2), Frac(3, 4))
        self.assertEqual(Frac(1, 9) - Frac(-2, 3), Frac(7, 9))
        self.assertEqual(Frac(-3, 5) - Frac(-1, 7), Frac(-16, 35))

    def test___mul__(self):
        self.assertEqual(Frac(3, 4) * Frac(-1, 3), Frac(1, -4))
        self.assertEqual(Frac(1, 1) * Frac(1, 2), Frac(1, 2))
        self.assertEqual(Frac(3, 1) * Frac(0, 1), Frac(0, 1))
        self.assertEqual(Frac(7, 2) * Frac(-5, 4), Frac(-35, 8))

    def test___truediv__(self):
        self.assertEqual(Frac(3, 4) / Frac(3, 2), Frac(1, 2))
        self.assertEqual(Frac(5, 1) / Frac(-1, 2), Frac(-10, 1))
        self.assertRaises(ZeroDivisionError, lambda: Frac(7, 5) / Frac(0, 1))

    def test___pos__(self):
        self.assertEqual(+Frac(2, 3), Frac(2, 3))
        self.assertEqual(+Frac(-3, 7), Frac(-3, 7))
        self.assertNotEqual(+Frac(-1, 3), Frac(1, 3))

    def test___neg__(self):
        self.assertEqual(-Frac(6, 4), Frac(-6, 4))
        self.assertEqual(-Frac(-1, 2), Frac(1, 2))
        self.assertEqual(-Frac(-7, -7), Frac(7, -7))
        self.assertNotEqual(-Frac(-7, -7), Frac(-7, -7))

    def test___invert__(self):
        self.assertEqual(~Frac(2, 1), Frac(1, 2))
        self.assertEqual(~Frac(1, -5), Frac(-5, 1))

    def test_lt(self):
        self.assertLess(Frac(1, 2), Frac(3, 5))
        self.assertLess(Frac(-1, 3), Frac(1, 77))

    def test_gt(self):
        self.assertGreater(Frac(6, 1), Frac(2, 1))
        self.assertGreater(Frac(0, 1), Frac(-1, 3))

    def test_le(self):
        self.assertLessEqual(Frac(2, 32), Frac(3,5))
        self.assertLessEqual(Frac(1, 2), Frac(1, 2))

    def test_ge(self):
        self.assertGreaterEqual(Frac(5, 10), Frac(1, 2))
        self.assertGreaterEqual(Frac(-1, 2), Frac(-1, 2))
        self.assertGreaterEqual(Frac(1, 3), Frac(-2, 1))

    def test_eq(self):
        self.assertEqual(Frac(1, 1), Frac(1, 1))
        self.assertEqual(Frac(0, 5), Frac(0, 1))
        self.assertEqual(Frac(1, 6), Frac(6, 36))
        self.assertNotEqual(Frac(1, 6), Frac(-6, 36))

    def test_ne(self):
        self.assertNotEqual(Frac(3, 2), Frac(2, 3))
        self.assertNotEqual(Frac(0, 1), Frac(1,1))
        self.assertNotEqual(Frac(7, 1), Frac(7, 5))

    def test___float__(self):
        self.assertEqual((Frac(1, 4)), 0.25)
        self.assertEqual((Frac(-5, 2)), -2.5)
        

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()