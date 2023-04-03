## Viikko 3

**29.3.2023**

- Koodin alustava rakenne on hahmoteltu [ohjelmistotekniikkakurssin Sokoban-esimerkin pohjalta](https://github.com/ohjelmistotekniikka-hy/pygame-sokoban)
- Pelin voi käynnistää ajamalla komennon "python src/index.py" projektin juuressa tai vaihtoehtoisesti komennolla "poetry invoke run start"
- Pelissä voi ohjata madon päätä nuolinäppäimillä
- "Mato" liikkuu automaattisesti tietyin väliajoin viimeisimpänä rekisteröityyn suuntaan
- Peli loppuu, kun "mato" osuu seinään

**30.3.2023**

- Pelin alussa kentälle syntyy omena, joka vaihtaa paikkaa satunnaiseen koordinaattiin kentällä törmäyksestä

**2.4.2023**

- Omena spawnaa kentästä riippumatta oikein
- Madon vartaloon liittyvää koodia lisätty, mutta ei vielä vaikutusta pelitilanteeseen
