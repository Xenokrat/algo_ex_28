import unittest
from football import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        res1 = Football([1, 3, 2], 3)
        res2 = Football([3, 2, 1], 3)
        res3 = Football([1, 7, 5, 3, 9], 5)
        res4 = Football([9, 5, 3, 7, 1], 5)
        res5 = Football([1, 4, 3, 2, 5], 5)
        self.assertTrue(res1)
        self.assertTrue(res2)
        self.assertTrue(res3)
        self.assertTrue(res5)

        self.assertFalse(res4)


if __name__ == '__main__':
    unittest.main()
