import unittest
from kassapaate import Kassapaate

class testKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_rahamaara_alustettu_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edulliset_lounaat_alustettu_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaat_lounaat_alustettu_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
