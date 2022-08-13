import unittest
from tank_rush import TankRush


class MyTestCase(unittest.TestCase):
    def test_tank_rush(self):
        res1 = TankRush(3, 4, '1234 2345 0987', 2, 2, '34 98')
        res2 = TankRush(5, 5, '12345 12345 12345 12345 09876',
                        3, 2, '34 34 87')

        res3 = TankRush(5, 5, '12345 12345 12345 12345 09876',
                        3, 2, '34 34 88')
        res4 = TankRush(3, 4, '1234 2345 0987', 3, 4, '1234 2345 0981')
        res5 = TankRush(3, 4, '1234 2345 0987', 2, 2, '45 87')
        res6 = TankRush(3, 4, '1234 2345 0987', 2, 2, '51 71')
        res7 = TankRush(3, 4, '1234 2345 0987', 2, 2, '87 00')
        self.assertEqual(res1, True)
        self.assertEqual(res2, True)  
        self.assertEqual(res3, False)  
        self.assertEqual(res4, False)  
        self.assertEqual(res5, True)  
        self.assertEqual(res6, False)
        self.assertEqual(res7, False)


if __name__ == '__main__':
    unittest.main()
