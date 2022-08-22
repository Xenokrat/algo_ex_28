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

    def test_can_reverse_sort(self):
        res1 = can_reverse_sort([10, 7, 5, 3, 9], 5)
        res2 = can_reverse_sort([1, 7, 5, 3, 9, 10, 11], 7)
        res3 = can_reverse_sort([1, 2, 3], 3)
        res4 = can_reverse_sort([3, 2, 1], 3)
        res5 = can_reverse_sort([9, 5, 3, 7, 1], 5)

        self.assertTrue(res2)
        self.assertTrue(res3)
        self.assertTrue(res4)

        self.assertFalse(res1)
        self.assertFalse(res5)

    def test_can_swap_sort(self):
        res1 = can_swap_sort([1, 3, 2], 3)
        res2 = can_swap_sort([3, 2, 1], 3)
        res3 = can_swap_sort([1, 6, 3, 4, 5, 2, 7], 7)
        res4 = can_swap_sort([1, 6, 3, 5, 4, 2, 7], 7)
        res5 = can_swap_sort([2, 4, 3, 1], 4)
        res6 = can_swap_sort([1, 2, 4, 3], 4)
        res7 = can_swap_sort([9, 5, 3, 7, 1], 5)


        self.assertTrue(res1)
        self.assertTrue(res2)
        self.assertTrue(res3)
        self.assertTrue(res6)

        self.assertFalse(res4)
        self.assertFalse(res5)
        self.assertFalse(res7)


if __name__ == '__main__':
    unittest.main()
