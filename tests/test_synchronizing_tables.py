import unittest
from synchronizing_tables import SynchronizingTables


class TestSynchronizingTables(unittest.TestCase):
    def test_synchronizing_tables(self):
        res1 = SynchronizingTables(4, [10, 67, 68, 28], [55, 73, 10, 6])
        res2 = SynchronizingTables(3, [50, 1, 1024], [20000, 100000, 90000])
        res3 = SynchronizingTables(4, [10, 5, 14, 18], [100, 200, 50, 75])
        res4 = SynchronizingTables(5, [4, 7, 3, 1, 6], [10, 30, 40, 20, 5])

        self.assertEqual(res1, [6, 55, 73, 10])
        self.assertEqual(res2, [90000, 20000, 100000])
        self.assertEqual(res3, [75, 50, 100, 200])
        self.assertEqual(res4, [20, 40, 10, 5, 30])
