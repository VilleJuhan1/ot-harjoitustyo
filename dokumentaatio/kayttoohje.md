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
