import unittest
from unmanned import Unmanned


class MyTestCase(unittest.TestCase):
    def test_unmanned(self):
        res1 = Unmanned(10, 2, [[3, 5, 5], [5, 2, 2]])

        res2 = Unmanned(20, 3,
                        [[7, 4, 2], [9, 2, 4], [13, 5, 4]]
                        )
        self.assertEqual(res1, 12)
        self.assertEqual(res2, 30)


if __name__ == '__main__':
    unittest.main()
