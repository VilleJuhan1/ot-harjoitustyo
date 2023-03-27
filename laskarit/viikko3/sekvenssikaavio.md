### Tehtävä 3: Sekvenssikaavio

```mermaid
sequenceDiagram

    participant main
    main->>auto: Machine()
    auto->>FuelTank: FuelTank()
    FuelTank->>auto: auto._tank.fuel_contents = 0

```
