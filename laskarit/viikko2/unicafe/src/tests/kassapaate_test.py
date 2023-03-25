import unittest
from kassapaate import Kassapaate

class testKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

#alustus

    def test_rahamaara_alustettu_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edulliset_lounaat_alustettu_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaat_lounaat_alustettu_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

#käteisosto toimii

    def test_kassan_rahamaara_kasvaa_kun_maksetaan_edullinen_lounas_kateisella(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_vaihtoraha_on_oikein_maksettaessa_kateisella_edullinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)

    def test_kassan_rahamaara_kasvaa_kun_maksetaan_maukas_lounas_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_vaihtoraha_on_oikein_maksettaessa_kateisella_maukas(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_edullisten_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukkaiden_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_rahat_palautuvat_edullisesti(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)

    def test_rahat_palautuvat_maukkaasti(self):
        pass

    def test_vaihtorahat_oikein_edullisesti(self):
        pass

    def test_vaihtorahat_oikein_maukkaasti(self):
        pass

    def test_edulliset_lounaat_ei_muutu_jos_ei_rahaa(self):
        pass

    def test_maukkaat_lounaat_ei_muutu_jos_ei_rahaa(self):
        pass

#maksukortteihin liittyvät testit
