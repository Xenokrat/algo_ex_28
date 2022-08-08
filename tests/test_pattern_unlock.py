import unittest
from pattern_unlock import PatternUnlock


class TestPatternUnlock(unittest.TestCase):
    def test_pattern_unlock(self):
        res1 = PatternUnlock(10, [1, 2, 3, 4, 5, 6, 2, 7, 8, 9])
        res2 = PatternUnlock(11, [6, 2, 1, 9, 8, 7, 2, 3, 4, 5, 1])
        res3 = PatternUnlock(9, [6, 2, 7, 8, 1, 5, 3, 4, 2])
        self.assertEqual(res1, '982843')
        self.assertEqual(res2, '1124264')
        self.assertEqual(res3, '148528')


if __name__ == '__main__':
    unittest.main()
