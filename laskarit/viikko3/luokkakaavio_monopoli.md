### Monopoli luokkakaaviona

```mermaid
classDiagram

%% Alustetaan luokat ja niiden suhteet
    Ruutu "*" --> "1" Pelilauta
    Pelaaja "*" --> "1" Ruutu
    Ruutu <|-- Vankila
    Ruutu <|-- Aloitus
    Ruutu <|-- 'Sattuma ja yhteismaa'
    Ruutu <|-- 'Asemat ja laitokset'
    Ruutu <|-- Kadut
    Toimintakortti "*" --> "*" 'Sattuma ja yhteismaa'

%% Määritetään yläluokkien ominaisuudet
    class Pelilauta{
    }
    class Ruutu{
        jarjestysnumero
        toiminto
    }
    class Pelaaja{
        pelinappula
        kortit
    }
```    
