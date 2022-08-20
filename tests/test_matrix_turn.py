import unittest
from matrix_turn import *


class MyTestCase(unittest.TestCase):
    # def test_matrix_turn(self):
    #     matrix = ["123456", "234567", "345678", "456789"]
    #     MatrixTurn(matrix, 4, 6, 3)
    #     self.assertListEqual(matrix, ['432123',
    #                                   '565434',
    #                                   '676754',
    #                                   '789876'])

    def test_make_circle_indexes(self):
        res = make_circle_indexes(3, 4)
        self.assertListEqual(res, [(0, 0), (0, 1), (0, 2), (0, 3),
                                   (1, 3), (2, 3),
                                   (2, 2), (2, 1), (2, 0),
                                   (1, 0)])

    def test_shift_circle(self):
        res = shift_circle([(0, 0), (0, 1), (0, 2), (0, 3)], 2)
        self.assertListEqual(res, [(0, 2), (0, 3), (0, 0), (0, 1)])


if __name__ == '__main__':
    unittest.main()
