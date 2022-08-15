import unittest
from mister_robot import *


class TestMisterRobot(unittest.TestCase):
    def test_mister_robot(self):
        res1 = MisterRobot(7, [1, 3, 4, 5, 2, 7, 6])
        res2 = MisterRobot(7, [1, 3, 4, 5, 6, 2, 7])
        res3 = MisterRobot(5, [4, 1, 5, 2, 3])
        res4 = MisterRobot(5, [1, 4, 3, 2, 5])
        self.assertTrue(res1)
        self.assertTrue(res2)
        self.assertFalse(res3)
        self.assertFalse(res4)

    def test_count_inversions(self):
        res1 = count_inversions(4, [8, 4, 2, 1])
        res2 = count_inversions(3, [3, 1, 2])
        self.assertEqual(res1, 6)
        self.assertEqual(res2, 2)


if __name__ == '__main__':
    unittest.main()
