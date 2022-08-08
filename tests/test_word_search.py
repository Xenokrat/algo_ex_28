import unittest
from word_search import WordSearch


class TestWordSearch(unittest.TestCase):
    def test_word_search(self):
        res1 = WordSearch(12, '1) строка разбивается на набор строк через выравнивание по заданной ширине.', 'выравнивание')
        res2 = WordSearch(5, 'Chromium OS дистрибутив операционной системы GNU/Linux', 'Chrom')

        self.assertEqual(res1, [0, 0, 0, 0, 1, 0, 0])  # add assertion here
        self.assertEqual(res2, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])  # add assertion here


if __name__ == '__main__':
    unittest.main()
