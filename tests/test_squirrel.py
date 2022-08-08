import unittest
from squirrel import squirrel
from squirrel_brute_force import squirrel_brute_force


class TestSquirrel(unittest.TestCase):
    def test_squirrel(self):
        res_sq = squirrel(5)  # 5! = 1
        res_sqb = squirrel_brute_force(5)
        self.assertEquals(res_sqb, res_sq)

