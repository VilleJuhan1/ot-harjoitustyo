## Viikko 7

**3.5.2023**

- Parhaat pelaajat pystyvät kirjoittamaan nimensä ennätystulosten listalle!

## Viikko 6

**30.4.2023**

- .csv-tiedoston lataaminen on muutettu ehdolliseksi käyttäen Devcommands()-luokkaa.
- Devcommands()-luokan avulla pelissä on mahdollista kokeilla uusia ominaisuuksia ilman, että perustoiminnallisuudet rikkoutuvat.
- Kehittäjätyökaluihin pääsee käyttämällä terminaalissa Poetry-komentoa "poetry run invoke devcommands"

**29.4.2023**

- Peli lataa kartan .csv-tiedostona Google Drivesta
- Poetry-komento oman linkin vaihtamiseksi karttatiedostoa varten tulossa myöhemmin

## Viikko 5

**23.4.2023**

- High score -lista toimii siten, että pelaajan tulokset tallentuvat sinne nimellä "Player"
- Ennätystulokset voi resetoida käyttämällä poetry-komentoa

**22.4.2023**

- Päävalikossa toimii nyt myös High score -valikko, josta pääsee pois mitä tahansa nappia painamalla. Tulokset eivät vielä päivity.

## Viikko 4

**9.4.2023**

- Päävalikko on integroitu onnistuneesti osaksi muuta peliä. Päävalikon toiminnallisuudet "New game" ja "Exit game" toimivat, kuten odottaa voi.

**7.4.2023**

- Päävalikkoa on hahmoteltu erilliseen main_menu.py-tiedostoon. Se kuitenkin vaatii vielä rakenteellisen uudistuksen omaksi luokakseen.

## Viikko 3

**2.4.2023**

- Omena spawnaa kentästä riippumatta oikein
- Madon vartaloon liittyvää koodia lisätty, mutta ei vielä vaikutusta pelitilanteeseen

**30.3.2023**

- Pelin alussa kentälle syntyy omena, joka vaihtaa paikkaa satunnaiseen koordinaattiin kentällä törmäyksestä

**29.3.2023**

- Koodin alustava rakenne on hahmoteltu [ohjelmistotekniikkakurssin Sokoban-esimerkin pohjalta](https://github.com/ohjelmistotekniikka-hy/pygame-sokoban)
- Pelin voi käynnistää ajamalla komennon "python src/index.py" projektin juuressa tai vaihtoehtoisesti komennolla "poetry invoke run start"
- Pelissä voi ohjata madon päätä nuolinäppäimillä
- "Mato" liikkuu automaattisesti tietyin väliajoin viimeisimpänä rekisteröityyn suuntaan
- Peli loppuu, kun "mato" osuu seinään
