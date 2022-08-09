import unittest
from conquest_campaign import ConquestCampaign


class TestConquestCampaign(unittest.TestCase):
    def test_conquest_campaign(self):
        print(ConquestCampaign(3, 4, 2, [2, 2, 3, 4]))
        self.assertEqual(ConquestCampaign(3, 4, 2, [2, 2, 3, 4]), 3)
