# Snek-matopeli

## Vaatimusmäärittely

### Sovelluksen tarkoitus

Sovellus on oma versio klassisesta matopelistä. Pelin tarkoituksena on kerätä kentälle ilmestyviä hedelmiä ja selviytyä mahdollisimman
pitkään.

### Käyttäjät

Pelissä ei ole erillisiä käyttäjärooleja.

### Käyttöliittymä

Peli avautuu aloitusvalikkoon, josta löytyvät seuraavat toiminnallisuudet:

- Aloita uusi peli
- Katso ennätystulokset
- Lopeta peli

Pelikenttä koodataan graafisena käyttäen Pygamea. Taustalla koodissa kaksiulotteinen taulukko. Mahdollisuus rakentaa näin myös uusia
kenttiä. Matoa ohjataan nuolinäppäimillä.

### Perusversion toiminnallisuudet

- [x] Tekstipohjainen käyttöliittymä
- [x] Paikalliseen tiedostoon tallentuvat ennätystulokset
- [x] Yksi pelattava kenttä, joka toimii yhdellä vaikeusasteella, kuten olettaa voi (liikkuminen, törmääminen, kasvaminen, hedelmien ilmestyminen ja pistelasku)
- [x] Perustoiminnallisuuksia testaavat automaattitestit

### Jatkokehittelyjä mahdollisuuksien mukaan

- [x] Graafinen aloitusvalikko
- [x] Virheiden huomiointi koodissa, esim. karttatiedostoa ladatessa
- [x] Uuden kirjaston käyttäminen koodissa
- [x] Tiedon tallentaminen ja lukeminen verkosta jossain muodossa (Tällä hetkellä vain karttatiedoston lukeminen)
- [ ] Vaikeusasteen vaihtaminen
- [ ] Madon ulkoasun vaihtaminen
- [x] Kentän vaihtaminen (Google Drive -linkin kautta)

### Toissijaisia, mutta kivoja tavoitteita

- [ ] Kaksinpeli
- [x] Kenttäeditori (Luomalla .csv-tiedosto ja tallentamalla se Google Driveen)
