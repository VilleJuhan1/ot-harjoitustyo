# Snek-matopeli

## Vaatimusmäärittely

### Sovelluksen tarkoitus

Sovellus on oma versio klassisesta matopelistä. Pelin tarkoituksena on kerätä kentälle ilmestyviä hedelmiä ja selviytyä mahdollisimman
pitkään.

### Käyttäjät

Pelissä ei ole erillisiä käyttäjärooleja.

### Käyttöliittymä

Peli avautuu graafiseen aloitusvalikkoon, josta löytyvät seuraavat toiminnallisuudet:

- Aloita uusi peli
- Katso ennätystulokset
- Lopeta peli

Valikossa liikutaan nuolinäppäimillä sekä ENTER- ja ESC-painikkeilla. Myös matoa ohjataan nuolinäppäimillä. Mikäli pelaaja saavuttaa riittävän
korkean tuloksen pelissä, kirjataan pelaajan haluama alias kirjoittamalla se. Kirjoittaminen ruudulle toimii, kuten olettaa saattaa.

### Tekniset ominaisuudet

Peli renderöidään käyttäen Pygame-kirjastoa. Pelihahmot, karttaelementit ja tekstit ovat Pygamen sprite-olioita. Pelikenttä ladataan kaksiulotteisesta taulukosta.

### Nykyisen julkaisun toiminnallisuudet

- [x] Graafinen käyttöliittymä
- [x] Paikalliseen tiedostoon tallentuvat ennätystulokset
- [x] Pelattava kenttä, joka toimii, kuten olettaa voi (liikkuminen, törmääminen, kasvaminen, hedelmien ilmestyminen ja pistelasku)
- [x] Perustoiminnallisuuksia testaavat automaattitestit
- [x] Karttatiedoston lukeminen Google Drivesta käyttäen kehittäjätyökaluja
- [x] Omien kenttien tekeminen luomalla parametrien mukainen .csv-tiedosto ja tallentamalla se Google Driveen
- [x] Virheiden huomiointi koodissa, esim. karttatiedostoa ladatessa

### Toiminnallisuudet, jotka jäivät odottamaan myöhempiä versioita

- [ ] Vaikeusasteen vaihtaminen
- [ ] Madon ulkoasun vaihtaminen
- [ ] Kaksinpeli
- [ ] Uuden, ennestään tuntemattoman kirjaston käyttäminen koodissa
