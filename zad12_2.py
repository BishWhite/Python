import unittest


def binarne_rek(L, left, right, y):
    
    if left <= right:
        k = (left + right) // 2
        if y == L[k]:
            return k
        if y > L[k]:
            return binarne_rek(L, k+1, right, y)
        else:
            return binarne_rek(L, left, k-1, y)
    return None


class TestBinRek(unittest.TestCase):

    def test_binarne_rek_1(self):
        L = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
        idx = binarne_rek(L, 0, len(L)-1, 1024)
        self.assertEqual(idx, 9)

    def test_binarne_rek_2(self):
        L = [1, 7, 9, 11, 13, 105, 107]
        idx = binarne_rek(L, 0, len(L)-1, 13)
        self.assertEqual(idx, 4)

    def test_binarne_rek_3(self):
        L = [-100, -5, 0, 109, 478, 88765, 987609]
        idx = binarne_rek(L, 0, len(L)-1, 0)
        self.assertEqual(idx, 2)

    


if __name__ == "__main__":
    unittest.main()