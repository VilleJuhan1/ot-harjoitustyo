### Monopoli luokkakaaviona

```mermaid
classDiagram
    Ruutu <|-- Vankila
    Ruutu <|-- Aloitus
    Ruutu <|-- Sattuma
    Ruutu <|-- Yhteismaa
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
    class Vankila{
    }
    class Aloitus{
    }
    class Sattuma{
    }
    class Yhteismaa{
    }
```    
