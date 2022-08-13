import unittest
from maximum_discount import MaximumDiscount


class MyTestCase(unittest.TestCase):
    def test_something(self):
        res = MaximumDiscount(7, [400, 350, 300, 250, 200, 150, 100])
        self.assertEqual(res, 450)


if __name__ == '__main__':
    unittest.main()
