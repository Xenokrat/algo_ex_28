import unittest
from bast_shoe import *


class MyTestCase(unittest.TestCase):
    def test_bast_shoe_add(self):
        res1 = BastShoe('1 Привет')
        self.assertEqual(res1, "Привет")

        res1 = BastShoe('1 , Мир!')
        self.assertEqual(res1, "Привет, Мир!")

        res1 = BastShoe('1 ++')
        self.assertEqual(res1, "Привет, Мир!++")

        res1 = BastShoe('2 2')
        self.assertEqual(res1, "Привет, Мир!")

        res1 = BastShoe('4')
        self.assertEqual(res1, "Привет, Мир!++")

        res1 = BastShoe('4')
        self.assertEqual(res1, "Привет, Мир!")

        res1 = BastShoe('1 *')
        self.assertEqual(res1, "Привет, Мир!*")

        res1 = BastShoe('4')
        self.assertEqual(res1, "Привет, Мир!")

        res1 = BastShoe('4')
        self.assertEqual(res1, "Привет, Мир!")

        res1 = BastShoe('4')
        self.assertEqual(res1, "Привет, Мир!")

        res1 = BastShoe('3 6')
        self.assertEqual(res1, ",")

        res1 = BastShoe('2 100')
        self.assertEqual(res1, "")

        res1 = BastShoe('1 Привет')
        self.assertEqual(res1, "Привет")

        res1 = BastShoe('1 , Мир!')
        self.assertEqual(res1, "Привет, Мир!")

        res1 = BastShoe('1 ++')
        self.assertEqual(res1, "Привет, Мир!++")

        res1 = BastShoe('4')
        self.assertEqual(res1, "Привет, Мир!")

        res1 = BastShoe('4')
        self.assertEqual(res1, "Привет")

        res1 = BastShoe('5')
        self.assertEqual(res1, "Привет, Мир!")

        res1 = BastShoe('4')
        self.assertEqual(res1, "Привет")

        res1 = BastShoe('5')
        self.assertEqual(res1, "Привет, Мир!")

        res1 = BastShoe('5')
        self.assertEqual(res1, "Привет, Мир!++")

        res1 = BastShoe('5')
        self.assertEqual(res1, "Привет, Мир!++")

        res1 = BastShoe('5')
        self.assertEqual(res1, "Привет, Мир!++")

        res1 = BastShoe('4')
        self.assertEqual(res1, "Привет, Мир!")

        res1 = BastShoe('4')
        self.assertEqual(res1, "Привет")

        res1 = BastShoe('2 2')
        self.assertEqual(res1, "Прив")

        res1 = BastShoe('4')
        self.assertEqual(res1, "Привет")

        res1 = BastShoe('5')
        self.assertEqual(res1, "Прив")

        res1 = BastShoe('5')
        self.assertEqual(res1, "Прив")

        res1 = BastShoe('5')
        self.assertEqual(res1, "Прив")


if __name__ == '__main__':
    unittest.main()
