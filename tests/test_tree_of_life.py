import unittest
from tree_of_life import TreeOfLife


class MyTestCase(unittest.TestCase):
    def test_something(self):
        res = TreeOfLife(3, 4, 12, ['.+..', '..+.', '.+..'])
        self.assertListEqual(res, ['.+..', '..+.', '.+..'])


if __name__ == '__main__':
    unittest.main()
