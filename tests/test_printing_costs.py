import unittest
from printing_costs import PrintingCosts


class MyTestCase(unittest.TestCase):
    def test_printing_costs(self):
        res1 = PrintingCosts('\\G[😀_+')
        res2 = PrintingCosts('C=/\'(fs~')
        res3 = PrintingCosts('m&g`}')
        self.assertEqual(res1, 97)
        self.assertEqual(res2, 107)
        self.assertEqual(res3, 97)


if __name__ == '__main__':
    unittest.main()
