import unittest
from tree_of_life import *


class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     res = TreeOfLife(3, 4, 5, ['.+..', '..+.', '.+..'])
    #     self.assertListEqual(res, ['.+..', '..+.', '.+..'])

    def test_parse_string(self):
        res = parse_string(['.+..', '..+.', '.+..'])
        self.assertListEqual(res, [[0, 1, 0, 0],
                                   [0, 0, 1, 0],
                                   [0, 1, 0, 0]])

    def test_parse_string_back(self):
        res = parse_string_back([[0, 1, 0, 0],
                                 [0, 0, 1, 0],
                                 [0, 1, 0, 0]])
        self.assertListEqual(res, ['.+..', '..+.', '.+..'])

    def test_even_year(self):
        res = even_year([[0, 1, 0, 0],
                         [0, 0, 1, 0],
                         [0, 1, 0, 0]], 3, 4)
        self.assertListEqual(res, [[1, 2, 1, 1],
                                   [1, 1, 2, 1],
                                   [1, 2, 1, 1]])


if __name__ == '__main__':
    unittest.main()
