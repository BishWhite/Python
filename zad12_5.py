import unittest


def moda_py(L, left, right):
    counter = {}
    while left <= right:
        counter[L[left]] = counter.get(L[left], 0) + 1
        left += 1
    return max(counter, key=counter.get)


class TestModa(unittest.TestCase):

    def test_moda_1(self):
        L = [2, 2, 1, 3, 1, 4, 2, 7, 1, 6, 1, 7, 2, 8, 2, 1, 4]
        self.assertEqual(moda_py(L, 0, len(L)-1), 2)

    def test_moda_2(self):
        L = [5, 2, 1, 5, 2, 1, 3, 3, 4, 4]
        self.assertEqual(moda_py(L, 0, len(L)-1), 5)


if __name__ == "__main__":
    unittest.main()