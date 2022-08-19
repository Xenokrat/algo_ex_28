import unittest
from sherlock_valid_string import *


class MyTestCase(unittest.TestCase):
    def test_sherlock_valid_string(self):
        res1 = SherlockValidString('xyzaa')
        res2 = SherlockValidString('xyz')
        res3 = SherlockValidString('xyazz')

        res4 = SherlockValidString('xyzzz')
        res5 = SherlockValidString('xxyyza')
        res6 = SherlockValidString('xxyyzabc')
        res7 = SherlockValidString('xxxyyyzz')

        self.assertTrue(res1)
        self.assertTrue(res2)
        self.assertTrue(res3)
        self.assertFalse(res4)
        self.assertFalse(res5)
        self.assertFalse(res6)
        self.assertFalse(res7)

    def test_make_char_map(self):
        res = make_char_map('xyzaa')
        self.assertDictEqual(res, {'x': 1,
                                   'y': 1,
                                   'z': 1,
                                   'a': 2})


if __name__ == '__main__':
    unittest.main()
