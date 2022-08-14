import unittest
from line_analysis import LineAnalysis


class TestLineAnalysis(unittest.TestCase):
    def test_line_analysis(self):
        res1 = LineAnalysis('*..*..*..*..*..*')
        res2 = LineAnalysis('*..*...*..*..*..*')
        res3 = LineAnalysis('*..*..*..*..**..*')
        res4 = LineAnalysis('*')
        res5 = LineAnalysis('***')
        res6 = LineAnalysis('.')
        res8 = LineAnalysis('*.......*.......*')
        res9 = LineAnalysis('**')
        res10 = LineAnalysis('*.*.*')
        self.assertEqual(res1, True)
        self.assertEqual(res2, False)
        self.assertEqual(res3, False)
        self.assertEqual(res4, True)
        self.assertEqual(res5, True)
        self.assertEqual(res6, False)
        self.assertEqual(res8, True)
        self.assertEqual(res9, True)
        self.assertEqual(res10, True)
