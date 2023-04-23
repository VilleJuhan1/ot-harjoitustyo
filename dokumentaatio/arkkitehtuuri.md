# Sovellusarkkitehtuuri

```mermaid
---
title: Kokonaisuus
---
classDiagram
    GameLoop <|.. Level
    GameLoop <|.. Renderer
    GameLoop <|.. EventQueue
    GameLoop <|.. Clock
    HighScore <|.. GameLoop
    Level <|.. Apple
    Level <|.. Body
    Level <|.. Floor
    Level <|.. Wall
    Level <|.. Worm
    Level <|.. Maps
    Menu .. GameLoop
    Menu .. HighScore
```
