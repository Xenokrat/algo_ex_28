import unittest
from matrix_turn import *


class MyTestCase(unittest.TestCase):
    def test_matrix_turn(self):
        matrix = ["123456", "234567", "345678", "456789"]
        MatrixTurn(matrix, 4, 6, 3)
        self.assertListEqual(matrix, ['432123',
                                      '565434',
                                      '676545',
                                      '789876'])

    def test_make_circle_indexes(self):
        matrix = ['1234',
                  '2345']
        matrix_copy = [list(i) for i in matrix]
        res = make_circle_indexes(matrix_copy, 2, 4, 0)
        self.assertListEqual(
            res,
            [[(0, 0), '1'], [(0, 1), '2'], [(0, 2), '3'], [(0, 3), '4'],
             [(1, 3), '5'], [(1, 2), '4'], [(1, 1), '3'], [(1, 0), '2']]
        )

    def test_rotate_circle(self):
        res = rotate_circle(
            [[(0, 0), '1'], [(0, 1), '2'], [(0, 2), '3'], [(0, 3), '4'],
             [(1, 3), '5'], [(1, 2), '4'], [(1, 1), '3'], [(1, 0), '2']],
            2
        )
        template = [
            [(0, 0), '3'], [(0, 1), '2'], [(0, 2), '1'], [(0, 3), '2'],
            [(1, 3), '3'], [(1, 2), '4'], [(1, 1), '5'], [(1, 0), '4']
        ]
        self.assertListEqual(
            res,
            template
        )


if __name__ == '__main__':
    unittest.main()
