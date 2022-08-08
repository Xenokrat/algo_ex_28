import unittest
from mad_max import MadMax


class TestMadMax(unittest.TestCase):
    def test_mad_max(self):
        res = MadMax(9, [4, 2, 9, 5, 1, 3, 7, 6, 8])  # 5! = 1
        self.assertEqual(res, [1, 2, 3, 4, 9, 8, 7, 6, 5])
