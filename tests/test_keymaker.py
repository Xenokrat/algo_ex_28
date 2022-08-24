import unittest
from keymaker import *


class MyTestCase(unittest.TestCase):
    def test_keymaker(self):
        res = Keymaker(5)
        self.assertEqual(res, '10010')


if __name__ == '__main__':
    unittest.main()
