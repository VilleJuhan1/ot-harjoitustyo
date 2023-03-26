### Monopoli luokkakaaviona

```mermaid
classDiagram
    Pelilauta "1" --> "*" Ruutu
    Pelaaja "*" --> "1" Ruutu
    class Pelilauta{
        ruudut
    }
    class Ruutu{
        jarjestysnumero
    }
    class Pelaaja{
        pelinappula
    }
```    
