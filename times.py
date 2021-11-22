import unittest

class Time:
    """Klasa reprezentująca odcinek czasu."""

    def __init__(self, s=0):
        """Zwraca instancję klasy Time."""
        if s < 0:
            raise ValueError("ujemny czas")
        self.s = int(s)

    def __str__(self):
        """Zwraca string 'hh:mm:ss'."""
        h = self.s // 3600
        sec = self.s - h * 3600
        m = sec // 60
        sec = sec - m * 60
        return "{0:02d}:{1:02d}:{2:02d}".format(h, m, sec)

    def __repr__(self):
        """Zwraca string 'Time(s)'."""
        return "Time({})".format(self.s)

    def __add__(self, other):
        """Dodawanie odcinków czasu."""
        return Time(self.s + other.s)

    def __cmp__(self, other): # Py2, porównywanie, -1|0|+1
        """Porównywanie odcinków czasu."""
        return cmp(self.s, other.s)

    # Py2.7 i Py3, rich comparisons.
    def __eq__(self, other):
        return self.s == other.s

    def __ne__(self, other):
        return self.s != other.s

    def __lt__(self, other):
        return self.s < other.s

    def __le__(self, other):
        return self.s <= other.s

    # nadmiarowe
    def __gt__(self, other):
        return self.s > other.s

    # nadmiarowe
    def __ge__(self, other):
        return self.s >= other.s

    def __int__(self):                  # int(time1)
        """Konwersja odcinka czasu do int."""
        return self.s

# Kod testujący moduł - dopisać co najmniej dwa testy do każdej sekcji.



class TestTime(unittest.TestCase):

    def setUp(self):
        self.t1 = Time(3723)
       

    def test_print(self):       # test str() i repr()
        self.assertEqual(str(self.t1), "01:02:03")
        self.assertEqual(repr(self.t1), "Time(3723)")
        self.assertEqual(str(Time(1)), '00:00:01')
        self.assertEqual(str(Time(75)), '00:01:15')
        self.assertEqual(repr(Time(100)), "Time(100)")

    def test_cmp(self):
        # Trzeba sprawdzać ==, !=, >, >=, <, <=.
        self.assertTrue(Time(2) == Time(2))
        self.assertFalse(Time(2) == Time(3))
        self.assertTrue(Time(2) != Time(3))
        self.assertFalse(Time(2) != Time(2))
        self.assertTrue(Time(2) < Time(3))
        self.assertFalse(Time(4) < Time(3))
        self.assertTrue(Time(2) <= Time(3))
        self.assertFalse(Time(4) <= Time(3))
        self.assertTrue(Time(4) > Time(3))
        self.assertFalse(Time(2) > Time(3))
        self.assertTrue(Time(4) >= Time(3))
        self.assertFalse(Time(2) >= Time(3))

    def test_add(self):
        self.assertEqual(Time(1) + Time(2), Time(3))
        self.assertEqual(Time(7) + Time(0), Time(7))
        self.assertNotEqual(Time(7) + Time(0), Time(10))

    def test_lt(self):
        self.assertTrue(Time(2) < Time(5))
        self.assertTrue(Time(5) < Time(32))
        self.assertFalse(Time(13) < Time(3))

    def test_gt(self):
        self.assertTrue(Time(4) > Time(2))
        self.assertTrue(Time(7) > Time(1))
        self.assertFalse(Time(3) > Time(5))

    def test_le(self):
        self.assertTrue(Time(6) <= Time(6))
        self.assertTrue(Time(3) <= Time(25))
        self.assertFalse(Time(10) <= Time(9))

    def test_ge(self):
        self.assertTrue(Time(3) >= Time(3))
        self.assertTrue(Time(6) >= Time(6))
        self.assertFalse(Time(4) >= Time(5))

    def test_eq(self):
        self.assertTrue(Time(0) == Time(0))
        self.assertTrue(Time(77) == Time(77))
        self.assertFalse(Time(1) == Time(7))

    def test_ne(self):
        self.assertTrue(Time(1) != Time(4))
        self.assertTrue(Time(100) != Time(2))
        self.assertFalse(Time(0) != Time(0))

    def test_int(self):
        self.assertEqual(int(Time(11)), 11)
        self.assertEqual(int(Time(1000)), 1000)
        self.assertNotEqual(int(Time(100)), 68)

    def tearDown(self):
        pass




if __name__ == "__main__":
    unittest.main()