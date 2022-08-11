import unittest
from mass_vote import MassVote


class MyTestCase(unittest.TestCase):
    def test_mass_vote(self):
        res1 = MassVote(5, [60, 10, 10, 15, 5])
        res2 = MassVote(3, [10, 15, 10])
        res3 = MassVote(5, [10, 15, 10, 25, 25])
        res4 = MassVote(4, [111, 111, 110, 110])
        self.assertEqual(res1, 'majority winner 1')
        self.assertEqual(res2, 'minority winner 2')
        self.assertEqual(res3, 'no winner')
        self.assertEqual(res4, 'no winner')


if __name__ == '__main__':
    unittest.main()
