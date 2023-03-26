### Monopoli luokkakaaviona

```mermaid
classDiagram
    Ruutu "*" --> "1" Pelilauta
    Pelaaja "*" --> "1" Ruutu
    class Pelilauta{
    }
    class Ruutu{
        jarjestysnumero
    }
    class Pelaaja{
        pelinappula
    }
```    
