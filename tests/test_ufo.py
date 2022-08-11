import unittest
from ufo import UFO


class MyTestCase(unittest.TestCase):
    def test_ufo(self):
        res1 = UFO(2, [1234, 1777], octal=False)
        res2 = UFO(2, [1234, 1777], octal=True)
        self.assertEqual(res1, [4660, 6007])
        self.assertEqual(res2, [668, 1023])


if __name__ == '__main__':
    unittest.main()
