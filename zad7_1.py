import unittest
from math import gcd


class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):

        if y == 0:
            raise ValueError('Mianownik musi być różny od 0')

        if y < 0:
            x, y = -x, -y


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

    @staticmethod
    def type_frac(arg):
        if isinstance(arg, Frac):
            return arg
        if isinstance(arg, int):
            return Frac(arg, 1)
        if isinstance(arg, float):
            return Frac(*arg.as_integer_ratio())

    def __add__(self, other):  # frac1 + frac2
        otf = Frac.type_frac(other)
        y = Frac._nww(self.y, otf.y)
        x = self.x * y // self.y + otf.x * y // otf.y
        return Frac(x, y).uprosc()

    __radd__ = __add__

    def __rsub__(self, other):  # int - frac, float - frac
        otf = Frac.type_frac(other)
        return -(self - otf).uprosc()

    def __sub__(self, other):  # frac1 - frac2
        otf = Frac.type_frac(other)
        y = Frac._nww(self.y, otf.y)
        x = self.x * y // self.y - otf.x * y // otf.y
        return Frac(x, y).uprosc()

    def __mul__(self, other):  # frac1 * frac2
        otf = Frac.type_frac(other)
        return Frac(self.x * otf.x, self.y * otf.y).uprosc()

    __rmul__ = __mul__

    def __truediv__(self, other):  # frac1 / frac2
        if other == 0:
            raise ZeroDivisionError('Dzielenie przez zero')
        otf = Frac.type_frac(other)    
        return Frac(self.x * otf.y, self.y * otf.x).uprosc()

    def __rtruediv__(self, other): # int / frac, float / frac
        otf = Frac.type_frac(other)
        return float(otf * ~self)

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
    
    def test___init__(self):
        self.assertEqual(Frac(5), Frac(5, 1))
        self.assertEqual(str(Frac(1, -2)), '-1/2')
        self.assertRaises(ValueError, lambda: Frac(4, 0))

    def test___str__(self):
        self.assertEqual(str(Frac(2, 2)), '2/2')
        self.assertEqual(str(Frac(-1, 77)), '-1/77')
        self.assertEqual(str(Frac(-1, -7)), '1/7')
        self.assertEqual(str(Frac(1, -4)), '-1/4')
        self.assertEqual(str(Frac(7, 2)), '7/2')
        self.assertNotEqual(str(Frac(1/5)),'1/4')
        self.assertEqual(str(Frac(4, 1)), '4')
        

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
        self.assertEqual(Frac(1, 2) + 2, Frac(5, 2))
        self.assertEqual(Frac(1, 2) + (-4), Frac(-7, 2))
        self.assertEqual(Frac(1, 2) + 0.5, Frac(1, 1))

    def test___radd__(self):
        self.assertEqual(Frac(1, 3) + Frac(1, 3), Frac(4, 6))
        self.assertEqual(Frac(3, 2) + Frac(6, 4), Frac(3, 1))
        self.assertEqual(Frac(-5,2)+ Frac(7,4), Frac(-3,4))
        self.assertEqual(Frac(-3, 2) + Frac(3, 2), Frac(0, 1))
        self.assertEqual(Frac(1, 2) + 2, Frac(5, 2))
        self.assertEqual(Frac(1, 2) + (-4), Frac(-7, 2))
        self.assertEqual(Frac(1, 2) + 0.5, Frac(1, 1))

    def test___sub__(self):
        self.assertEqual(Frac(3, 4) - Frac(3, 4), Frac(0, 2))
        self.assertEqual(Frac(5, 4) - Frac(1, 2), Frac(3, 4))
        self.assertEqual(Frac(1, 9) - Frac(-2, 3), Frac(7, 9))
        self.assertEqual(Frac(-3, 5) - Frac(-1, 7), Frac(-16, 35))
        self.assertEqual(Frac(3, 4) - 1, Frac(-1, 4))
        self.assertEqual(Frac(1, 2) - 0.75, Frac(-1, 4))

    def test___rsub__(self):
        self.assertEqual(Frac(3, 4) - Frac(3, 4), Frac(0, 2))
        self.assertEqual(Frac(5, 4) - Frac(1, 2), Frac(3, 4))
        self.assertEqual(Frac(1, 9) - Frac(-2, 3), Frac(7, 9))
        self.assertEqual(Frac(-3, 5) - Frac(-1, 7), Frac(-16, 35))
        self.assertEqual(Frac(3, 4) - 1, Frac(-1, 4))
        self.assertEqual(Frac(1, 2) - 0.75, Frac(-1, 4))


    def test___mul__(self):
        self.assertEqual(Frac(3, 4) * Frac(-1, 3), Frac(1, -4))
        self.assertEqual(Frac(1, 1) * Frac(1, 2), Frac(1, 2))
        self.assertEqual(Frac(3, 1) * Frac(0, 1), Frac(0, 1))
        self.assertEqual(Frac(7, 2) * Frac(-5, 4), Frac(-35, 8))
        self.assertEqual(Frac(3, 4) * 4, Frac(3, 1))
        self.assertEqual(Frac(4, 3) * 0.5, Frac(2, 3))

    def test___rmul__(self):
        self.assertEqual(Frac(3, 4) * Frac(-1, 3), Frac(1, -4))
        self.assertEqual(Frac(1, 1) * Frac(1, 2), Frac(1, 2))
        self.assertEqual(Frac(3, 1) * Frac(0, 1), Frac(0, 1))
        self.assertEqual(Frac(7, 2) * Frac(-5, 4), Frac(-35, 8))
        self.assertEqual(Frac(3, 4) * 4, Frac(3, 1))
        self.assertEqual(Frac(4, 3) * 0.5, Frac(2, 3))
  

    def test___truediv__(self):
        self.assertEqual(Frac(3, 4) / Frac(3, 2), Frac(1, 2))
        self.assertEqual(Frac(5, 1) / Frac(-1, 2), Frac(-10, 1))
        self.assertRaises(ZeroDivisionError, lambda: Frac(7, 5) / Frac(0, 1))
        self.assertEqual(Frac(3, 2) / 2, Frac(3, 4))
        self.assertEqual(Frac(3, 1) / 1.5, Frac(2, 1))

    def test__rtruediv__(self):
        self.assertEqual(Frac(3, 4) / Frac(3, 2), Frac(1, 2))
        self.assertEqual(Frac(5, 1) / Frac(-1, 2), Frac(-10, 1))
        self.assertRaises(ZeroDivisionError, lambda: Frac(7, 5) / Frac(0, 1))
        self.assertEqual(Frac(3, 2) / 2, Frac(3, 4))
        self.assertEqual(Frac(3, 1) / 1.5, Frac(2, 1))


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