import unittest
from odometer import odometer


class TestOdometer(unittest.TestCase):
    def test_odometer(self):
        res_od = odometer([10, 1, 20, 2, 30, 4, 20, 6])  # = 30
        self.assertEquals(res_od, 130)
