import unittest
from abr_vs_arn import *
import sys

sys.setrecursionlimit(1050)


class TestCase(unittest.TestCase):
    def setUp(self):
        keys = []
        for i in range(0, 1000):
            keys.append(i)
        self.abrwc = Abr(keys)
        self.arnwc = Arn(keys)
        random.shuffle(keys)
        self.abr1 = Abr(keys)
        self.arn1 = Arn(keys)
        random.shuffle(keys)
        self.abr2 = Abr(keys)
        self.arn2 = Arn(keys)
        random.shuffle(keys)
        self.abr3 = Abr(keys)
        self.arn3 = Arn(keys)
        random.shuffle(keys)
        self.abr4 = Abr(keys)
        self.arn4 = Arn(keys)
        random.shuffle(keys)
        self.abr5 = Abr(keys)
        self.arn5 = Arn(keys)

    def test_height(self):
        height_abrwc = self.abrwc.height(self.abrwc.get_root_key())
        print("L'altezza dell'albero binario di ricerca  nel caso peggiore con ", self.abrwc.get_length(), " elementi è ", height_abrwc)
        self.assertEqual(height_abrwc, 1000)
        height_arnwc = self.arnwc.height(self.arnwc.get_root())
        print("L'altezza dell'albero rosso-nero nel caso peggiore con ", self.arnwc.get_length(), " elementi è ", height_arnwc)
        self.assertLessEqual(height_arnwc, height_abrwc)
        height_abr1 = self.abr1.height(self.abr1.get_root_key())
        print("L'altezza dell'albero binario di ricerca con ", self.abr1.get_length(), " elementi è ", height_abr1)
        height_arn1 = self.arn1.height(self.arn1.get_root())
        print("L'altezza dell'albero rosso nero con ", self.arn1.get_length(), " elementi è ", height_arn1)
        self.assertLessEqual(height_arn1, height_abr1)
        height_abr2 = self.abr2.height(self.abr2.get_root_key())
        print("L'altezza dell'albero binario di ricerca con ", self.abr2.get_length(), " elementi è ", height_abr2)
        height_arn2 = self.arn2.height(self.arn2.get_root())
        print("L'altezza dell'albero rosso nero con ", self.arn2.get_length(), " elementi è ", height_arn2)
        self.assertLessEqual(height_arn2, height_abr2)
        height_abr3 = self.abr3.height(self.abr3.get_root_key())
        print("L'altezza dell'albero binario di ricerca con ", self.abr3.get_length(), " elementi è ", height_abr3)
        height_arn3 = self.arn3.height(self.arn3.get_root())
        print("L'altezza dell'albero rosso nero con ", self.arn3.get_length(), " elementi è ", height_arn3)
        self.assertLessEqual(height_arn3, height_abr3)
        height_abr4 = self.abr4.height(self.abr4.get_root_key())
        print("L'altezza dell'albero binario di ricerca con ", self.abr4.get_length(), " elementi è ", height_abr4)
        height_arn4 = self.arn4.height(self.arn4.get_root())
        print("L'altezza dell'albero rosso nero con ", self.arn4.get_length(), " elementi è ", height_arn4)
        self.assertLessEqual(height_arn4, height_abr4)
        height_abr5 = self.abr5.height(self.abr5.get_root_key())
        print("L'altezza dell'albero binario di ricerca con ", self.abr5.get_length(), " elementi è ", height_abr5)
        height_arn5 = self.arn5.height(self.arn5.get_root())
        print("L'altezza dell'albero rosso nero con ", self.arn5.get_length(), " elementi è ", height_arn5)
        self.assertLessEqual(height_arn5, height_abr5)


if __name__ == '__main__':
    unittest.main()
