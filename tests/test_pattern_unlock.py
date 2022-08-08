import unittest
from pattern_unlock import PatternUnlock


class TestPatternUnlock(unittest.TestCase):
    def test_pattern_unlock(self):
        res = PatternUnlock(10, [1, 2, 3, 4, 5, 6, 2, 7, 8, 9])
        self.assertEqual(res, '982843')


if __name__ == '__main__':
    unittest.main()
