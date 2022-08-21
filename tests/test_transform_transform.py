import unittest
from transform_transform import *


class MyTestCase(unittest.TestCase):
    def test_transform(self):
        res1 = TransformTransform([3, 4], 2)
        res2 = TransformTransform([3, 4, 5], 3)
        self.assertFalse(res1)
        self.assertTrue(res2)


if __name__ == '__main__':
    unittest.main()
