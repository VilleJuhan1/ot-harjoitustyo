# Snek-matopeli

## Vaatimusmäärittely

### Sovelluksen tarkoitus

Sovellus on oma versio klassisesta matopelistä. Pelin tarkoituksena on kerätä kentälle ilmestyviä hedelmiä ja selviytyä mahdollisimman
pitkään.

### Käyttäjät

Pelissä ei ole erillisiä käyttäjärooleja.

### Käyttöliittymä

Peli avautuu aloitusvalikkoon, josta löytyvät ainakin seuraavat toiminnallisuudet:

- Aloita uusi peli
- Vaihda vaikeusastetta (1-9)
- Katso ennätystulokset
- Lopeta peli

Pelikenttä koodataan graafisena käyttäen Pygamea. Taustalla koodissa kaksiulotteinen taulukko. Mahdollisuus rakentaa näin myös uusia
kenttiä. Matoa ohjataan nuolinäppäimillä.

### Perusversion toiminnallisuudet

- [x] Tekstipohjainen käyttöliittymä
- [ ] Paikalliseen tiedostoon tallentuvat ennätystulokset
- [x] Yksi pelattava kenttä, joka toimii yhdellä vaikeusasteella, kuten olettaa voi (liikkuminen, törmääminen, kasvaminen, hedelmien ilmestyminen ja pistelasku)
- [ ] Perustoiminnallisuuksia testaavat automaattitestit

### Jatkokehittelyjä mahdollisuuksien mukaan

- [x] Graafinen aloitusvalikko
- [ ] Vaikeusasteen vaihtaminen
- [ ] Madon ulkoasun vaihtaminen
- [ ] Kentän vaihtaminen
- [ ] Globaali high score -lista

### Toissijaisia, mutta kivoja tavoitteita

- [ ] Kaksinpeli
- [ ] Kenttäeditori
