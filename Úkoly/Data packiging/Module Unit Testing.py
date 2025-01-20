# TASK 2

import unittest


class TestCislo(unittest.TestCase):

    def test_zapisy_a_cteni(self):
        c = Cislo(10)
        self.assertEqual(c.get_hodnota(), 10)
        c.set_hodnota(20)
        self.assertEqual(c.get_hodnota(), 20)

    def test_na_osmicovou(self):
        c = Cislo(10)
        self.assertEqual(c.na_osmicovou(), '12')  # 10 v osmičkové soustavě je 12

        c = Cislo(64)
        self.assertEqual(c.na_osmicovou(), '100')  # 64 v osmičkové soustavě je 100

    def test_na_sestnactkovou(self):
        c = Cislo(10)
        self.assertEqual(c.na_sestnactkovou(), 'a')  # 10 v šestnáctkové soustavě je a

        c = Cislo(255)
        self.assertEqual(c.na_sestnactkovou(), 'ff')  # 255 v šestnáctkové soustavě je ff

    def test_na_binarni(self):
        c = Cislo(10)
        self.assertEqual(c.na_binarni(), '1010')  # 10 v binární soustavě je 1010

        c = Cislo(64)
        self.assertEqual(c.na_binarni(), '1000000')  # 64 v binární soustavě je 1000000


if __name__ == "__main__":
    unittest.main()
