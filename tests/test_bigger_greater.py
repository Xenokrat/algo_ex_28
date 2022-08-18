import unittest
from bigger_greater import BiggerGreater


class MyTestCase(unittest.TestCase):
    def test_bigger_greater(self):
        res1 = BiggerGreater('вибк')
        res2 = BiggerGreater('fff')
        res3 = BiggerGreater('нклм')
        res4 = BiggerGreater('ая')
        res5 = BiggerGreater('вкиб')
        res6 = BiggerGreater('looool')
        self.assertEqual(res1, 'викб')
        self.assertEqual(res2, '')
        self.assertEqual(res3, 'нкмл')
        self.assertEqual(res4, 'яа')
        self.assertEqual(res5, 'ибвк')
        self.assertEqual(res6, 'ollooo')


if __name__ == '__main__':
    unittest.main()
