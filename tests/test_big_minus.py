import unittest
from big_minus import BigMinus


class TestBigMinus(unittest.TestCase):
    def test_big_minus(self):
        res1 = BigMinus("1234567891", "1")
        res2 = BigMinus("1", "1")
        res3 = BigMinus("1", "321")
        res4 = BigMinus("46546461", "546613616")
        self.assertEqual(res1, "1234567890")
        self.assertEqual(res2, "0")
        self.assertEqual(res3, "320")
        self.assertEqual(res4, "500067155")


if __name__ == '__main__':
    unittest.main()
