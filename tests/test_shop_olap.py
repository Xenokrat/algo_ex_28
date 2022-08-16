import unittest
from shop_olap import *


class MyTestCase(unittest.TestCase):
    def test_shop_olap(self):
        res1 = ShopOLAP(5, ['платье1 5', 'сумка32 2', 'платье1 1',
                            'сумка23 2', 'сумка128 4'])
        self.assertListEqual(res1, ['платье1 6', 'сумка128 4',
                                    'сумка23 2', 'сумка32 2'])

    def test_make_dict(self):
        res = make_dict(['платье1 5', 'сумка32 2', 'платье1 1',
                         'сумка23 2', 'сумка128 4'])
        self.assertEqual(res, {'платье1': 6, 'сумка128': 4,
                               'сумка23': 2, 'сумка32': 2})

    def test_sort_items(self):
        res = sort_items({'сумка32': 2, 'сумка128': 4,
                          'платье1': 6, 'сумка23': 2})
        self.assertListEqual(res, [('платье1', 6), ('сумка128', 4),
                                   ('сумка23', 2), ('сумка32', 2)])


if __name__ == '__main__':
    unittest.main()
