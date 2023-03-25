import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class testKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

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
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100), 100)

    def test_kassa_ei_muutu_jos_maksu_ei_riita_edulliseen(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassa_ei_muutu_jos_maksu_ei_riita_maukkaaseen(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edulliset_lounaat_ei_muutu_jos_ei_rahaa(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaat_lounaat_ei_muutu_jos_ei_rahaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.maukkaat, 0)

#maksukortteihin liittyvät testit

    def test_korttiosto_edullinen_lounas_saldo(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 760)

    def test_edullisten_maara_kasvaa_kortilla(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_korttiosto_onnistuu_edullisesti_kortilla(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_korttiosto_maukas_lounas_saldo(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 600)

    def test_maukkaiden_maara_kasvaa_kortilla(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_korttiosto_onnistuu_maukkaasti_kortilla(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_kassassa_oleva_rahamaara_ei_muutu_kortilla_maksettaessa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttimaksu_ei_onnistu_edullisesti(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 100)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)

    def test_korttimaksu_ei_onnistu_maukkaasti(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 100)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)

    def test_kortille_ladattaessa_saldo_muuttuu_ja_kassan_rahamaara_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.maksukortti.saldo, 2000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    def test_kortilla_yritetaan_ladata_negatiivinen_summa_rahaa(self):
        self.assertEqual(self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000), None)

