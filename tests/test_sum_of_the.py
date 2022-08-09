import unittest
from sum_of_the import SumOfThe


class TestSumOfThe(unittest.TestCase):
    def test_sum_of_the(self):
        res1 = SumOfThe(7, [100, -50, 10, -25, 90, -35, 90])
        res2 = SumOfThe(5, [10, -25, -45, -35, 5])
        self.assertEqual(res1, 90)  # add assertion here
        self.assertEqual(res2, -45)  # add assertion here


if __name__ == '__main__':
    unittest.main()
