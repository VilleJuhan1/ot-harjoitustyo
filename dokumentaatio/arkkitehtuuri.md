# Sovellusarkkitehtuuri

```mermaid
---
title: Snek-matopeli
---
classDiagram
    GameLoop <|.. Level
    GameLoop <|.. Renderer
    GameLoop <|.. EventQueue
    GameLoop <|.. Clock
    Level <|.. Apple
    Level <|.. Body
    Level <|.. Floor
    Level <|.. Wall
    Level <|.. Worm
    Level <|.. Maps
    Menu .. GameLoop
```
