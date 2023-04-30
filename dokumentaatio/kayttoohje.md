# Käyttöohje

Kloonaa projekti itsellesi gitillä tai lataa viimeisin julkaisuversio [täältä](https://github.com/VilleJuhan1/ot-harjoitustyo/releases).

## Asennus

Asenna riippuvuudet komennolla:

> poetry install

## Snek-matopeli

Käynnistä sovellus komennolla:

> poetry run invoke start

### Päävalikko

Peli käynnistyy päävalikkoon. Valitse haluamasi toiminto nuolinäppäimillä ja enterillä.

![image of the main menu](https://github.com/VilleJuhan1/ot-harjoitustyo/blob/master/dokumentaatio/kuvatiedostot/menu.png)

### Ennätystulokset

Valitsemalla päävalikosta kohdan "High Score" pääset tarkastelemaan ennätystuloksia. Pääset pois tuloksista painamalla mitä tahansa näppäintä.

![image of the high score menu](https://github.com/VilleJuhan1/ot-harjoitustyo/blob/master/dokumentaatio/kuvatiedostot/highscore.png)

Voit nollata ennätystulokset oletusasetuksille komennolla:

> poetry run invoke reset-score

### Pelaaminen

Uusi peli alkaa välittömästi valittaessa päävalikosta "New Game". Liikuta matoa nuolinäppäimillä. Keräämällä omenoita saat pisteitä. Peli
loppuu, jos törmäät omaan häntääsi (vaaleanvihreä) tai seinään (harmaa).

![image of the game](https://github.com/VilleJuhan1/ot-harjoitustyo/blob/master/dokumentaatio/kuvatiedostot/gameplay.png)

## Kehittäjän työkalut

Pelissä on tiettyjä ominaisuuksia, jotka ovat käytössä vain eräänlaisessa kehittäjäversiossa. Pääset kehittäjätyökaluihin komennolla:

> Poetry run invoke devcommands

Työkalut avautuvat terminaalissa tiedostosta src/game/devcommands.py. Tällä hetkellä käytössä ovat:

1. mode: Vaihtamalla tilaksi 'online', peli lataa kartan Google Drivessa olevasta .csv-tiedostosta.
2. url: Vaihtamalla osoitteen, voit ladata uusia .csv-tiedostoja Google Drivesta ja kokeilla peliä niillä. [Esimerkkitiedosto](https://drive.google.com/file/d/1ZsHfubrB7LQwKMvhbGr_UNvfk_GHJcix/view?usp=share_link).
3. reset: Palauttaa oletusasetukset eli nollaa moden ja urlin.
