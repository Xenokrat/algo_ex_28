import unittest
from the_rabbits_foot import TheRabbitsFoot


class TestTheRabbitsFoot(unittest.TestCase):
    def test_the_rabbits_foot_encode(self):
        res_encode = TheRabbitsFoot('отдай мою кроличью лапку', encode=True)
        self.assertEqual(res_encode, 'омоюу толл дюиа акчп йрьк')

    def test_the_rabbits_foot_decode(self):
        res_decode = TheRabbitsFoot('омоюу толл дюиа акчп йрьк', encode=False)
        self.assertEqual(res_decode, 'отдаймоюкроличьюлапку')

    def test_the_rabbits_foot_reverse(self):
        res1 = TheRabbitsFoot('отдай мою кроличью лапку', encode=True)
        res2 = TheRabbitsFoot(res1, encode=False)
        self.assertEqual(res2, 'отдаймоюкроличьюлапку')

    def test_the_vin_disel_reverse(self):
        res1 = TheRabbitsFoot('все ищут острых ощущений '
                              'но самое важное лишь семья', encode=True)
        res2 = TheRabbitsFoot(res1, encode=False)
        self.assertEqual(res2, 'всеищутострыхощущенийносамоеважноелишьсемья')


if __name__ == '__main__':
    unittest.main()
