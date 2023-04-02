# OT2023 harjoitustyö

Tämä projekti on Helsingin yliopiston kevään 2023 Ohjelmistotekniikka-kurssiin liittyvä harjoitustyö. Repositoriossa on sekä kurssiin liittyviä
[harjoitustehtäviä](https://github.com/VilleJuhan1/ot-harjoitustyo/tree/master/laskarit) että oma ohjelmointiprojekti.

Ohjelmointiprojektin rakenteellisena runkona on käytetty kurssin [Sokoban-esimerkkiä](https://github.com/ohjelmistotekniikka-hy/pygame-sokoban).

## Snek-matopeli

Peli on tällä hetkellä kehitysvaiheessa. Nykyisessä versiossa peli alkaa aloituskomennolla, minkä jälkeen "mato" on ohjattavissa nuolinäppäimillä.
Törmäys punaiseen omenaan aiheuttaa sen siirtymisen uuteen koordinaattiin. Törmäys seinään lopettaa pelin.

### Kontrollit

Ohjaa matoa nuolinäppäimillä. ESC lopettaa pelin.

### Dokumentaatio
* [Alustava määrittelydokumentti](https://github.com/VilleJuhan1/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
* [Työaikakirjanpito](https://github.com/VilleJuhan1/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)
* [Changelog](https://github.com/VilleJuhan1/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)
##### Asennus
> poetry install
##### Suorittaminen
> poetry run invoke start
##### Testaaminen
> poetry run invoke coverage-report
