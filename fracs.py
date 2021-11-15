import unittest
from math import gcd 

def nww(a, b):

    return abs(a * b) // gcd(a, b)

def uprosc(frac):

    licznik, mianownik = frac[0], frac[1]
    nwdzielnik = gcd(licznik, mianownik)

    if mianownik > 0:
        return [licznik // nwdzielnik, mianownik // nwdzielnik]
    return [-licznik // nwdzielnik, -mianownik // nwdzielnik]

def add_frac(frac1, frac2):
    mianownik = nww(frac1[1], frac2[1])
    licznik = frac1[0] * mianownik // frac1[1] + frac2[0] * mianownik // frac2[1]
    return uprosc([licznik, mianownik])


def sub_frac(frac1, frac2):
    mianownik = nww(frac1[1], frac2[1])
    licznik = frac1[0] * mianownik // frac1[1] - frac2[0] * mianownik // frac2[1]
    return uprosc([licznik,mianownik])

def mul_frac(frac1, frac2):
    return uprosc([frac1[0] * frac2[0], frac1[1] * frac2[1]])

def div_frac(frac1,frac2):
    if is_zero(frac2):
        raise ValueError('Dzielenie przez zero')

    return mul_frac(frac1, [frac2[1], frac2[0]])


def is_positive(frac):
    if (frac[0] > 0 and frac[1] > 0) or (frac[0] < 0 and frac[1] < 0):
        return True
    return False


def is_zero(frac):
    if frac[0] == 0:
        return True
    return False

def cmp_frac(frac1, frac2):
    abs1 = sub_frac([abs(frac1[0]), abs(frac1[1])],[abs(frac2[0]), abs(frac2[1])])
    if abs1[0] > 0:
        return 1
    if abs1[0] == 0:
        return 0
    return -1


def frac2float(frac):
    return frac[0] / frac[1]


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([1, 2], [1, 4]), [3, 4])
        self.assertEqual(add_frac([-3, 2], [3, 2]), [0, 1])
    def test_sub_frac(self):
        self.assertEqual(sub_frac([3, 1], [4, 1]), [-1, 1])
        self.assertEqual(sub_frac([1, 4], [4, 2]), [-7, 4])
        self.assertEqual(sub_frac([1, 3], [1, 3]), [0, 1])
        self.assertEqual(sub_frac([-2, 1], [-3, 4]), [-5, 4])


    def test_mul_frac(self): 
        self.assertEqual(mul_frac([5, 2], [1, 2]), [5, 4])
        self.assertEqual(mul_frac([1, 2], [0, 2]), [0, 1])
        self.assertEqual(mul_frac([2, 5], [-2, 4]), [-1, 5])

    def test_div_frac(self): 
        self.assertEqual(div_frac([3, 4], [3, 1]), [1, 4])
        self.assertEqual(div_frac([1, 1], [-1, 2]), [-2, 1])
        self.assertRaises(ValueError, lambda: div_frac([1, 3], [0, 5]))

    def test_is_positive(self): 
        self.assertTrue(is_positive([1, 10]))
        self.assertTrue(is_positive([-1, -10]))
        self.assertFalse(is_positive([-1, 5]))
        self.assertFalse(is_positive([1, -5]))

    def test_is_zero(self): 
        self.assertTrue(is_zero([0, 1]))
        self.assertFalse(is_zero([1, 5]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([5, 2], [1, 2]), 1)
        self.assertEqual(cmp_frac([1, 2], [7, 2]), -1)
        self.assertEqual(cmp_frac([5, 1], [10, 2]), 0)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 4]), 0.25)
        self.assertEqual(frac2float([-5, 2]), -2.5)

    def tearDown(self): pass

    


if __name__ == '__main__':
    unittest.main()