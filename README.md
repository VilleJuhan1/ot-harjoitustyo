# OT2023 harjoitustyö

Tämä projekti on Helsingin yliopiston kevään 2023 Ohjelmistotekniikka-kurssiin liittyvä harjoitustyö. Repositoriossa on sekä kurssiin liittyviä
[harjoitustehtäviä](https://github.com/VilleJuhan1/ot-harjoitustyo/tree/master/laskarit) että oma ohjelmointiprojekti (Snek-matopeli).

Pelin rakenteellisena runkona on käytetty kurssin [Sokoban-esimerkkiä](https://github.com/ohjelmistotekniikka-hy/pygame-sokoban).

## Snek-matopeli

Pelin perustoiminnallisuudet ovat valmiit!

Sovellus käynnistyy päävalikkoon aloituskomennolla "poetry run invoke start". Pelin tarkoituksena on kerätä punaisia omenoita ja välttää törmäyksiä madon häntään ja seiniin. Tavoitteena on kasvaa mahdollisimman suureksi. Parhaat tulokset tallentuvat ennätystauluun, jonka voi halutessaan alustaa käyttämällä poetry-komentoa "poetry run invoke reset-score".

Lähdekoodissa on mukana myös kehittäjätyökalut, joiden avulla pystyy vaihtamaan pelimuodon onlineksi. Tällä hetkellä ainoa vaikutus kuitenkin on,
että pelin kartta latautuu Google Drivessa olevasta .csv-tiedostosta. Kehittäjätyökalujen avulla tiedostopolku on mahdollista muuttaa haluamakseen. Peli
ei kuitenkaan hyväksy muita kuin Google Drive -linkkejä.

### Kontrollit

Ohjaa matoa ja päävalikon kursoria nuolinäppäimillä. Halutessasi voit poistua pelistä ESC-näppäimellä. Ennätystulostaulusta poistuminen
tapahtuu millä tahansa näppäimellä.

### Dokumentaatio

* [Alustava määrittelydokumentti](https://github.com/VilleJuhan1/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
* [Työaikakirjanpito](https://github.com/VilleJuhan1/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)
* [Changelog](https://github.com/VilleJuhan1/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
* [Arkkitehtuuri](https://github.com/VilleJuhan1/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
* [Käyttöohje](https://github.com/VilleJuhan1/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

### Julkaistut versiot

[Viikko 6](https://github.com/VilleJuhan1/ot-harjoitustyo/releases/tag/viikko6)

[Viikko 5](https://github.com/VilleJuhan1/ot-harjoitustyo/releases/tag/viikko5)

### Tarvittavat komennot

##### Asennus
> poetry install
##### Suorittaminen
> poetry run invoke start
##### Testaaminen
> poetry run invoke coverage-report
##### Pylint-tarkistusten tekeminen
> poetry run invoke lint
##### Ennätystaulun alustaminen
> poetry run invoke reset-score
##### Kehittäjätyökalut (edistyneille käyttäjille)
> poetry run invoke devcommands
