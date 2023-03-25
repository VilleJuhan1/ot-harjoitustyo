import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

#Tehtävän 6 testit

    def test_saldo_alussa_oikein(self):
        kortti = self.maksukortti

        self.assertEqual(str(kortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")

    def test_saldo_vahenee_oikein_kun_rahaa_riittavasti(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")

    def test_saldo_ei_muutu_jos_rahaa_ei_riittavasti(self):
        self.maksukortti.ota_rahaa(2000)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_ota_rahaa_palauttaa_True_jos_rahat_riittivat(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)

    def test_ota_rahaa_palauttaa_False_jos_rahat_eivat_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(2000), False)
