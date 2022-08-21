import unittest
from white_walkers import *


class MyTestCase(unittest.TestCase):
    def test_white_walkers(self):
        res1 = white_walkers('axxb6===4xaf5===eee5')
        res2 = white_walkers('5==ooooooo=5=5')
        res3 = white_walkers('abc=7==hdjs=3gg1=======5')
        res4 = white_walkers('aaS=8')
        res5 = white_walkers('9===1===9===1===9')

        self.assertTrue(res1)
        self.assertTrue(res3)
        self.assertTrue(res5)

        self.assertFalse(res2)
        self.assertFalse(res4)


if __name__ == '__main__':
    unittest.main()
