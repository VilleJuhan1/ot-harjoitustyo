def reset_highscore(file="src/menu/scores.txt"):
    default_values = [("Mauno", 500), ("Rauno", 400),
                      ("Pauli", 300), ("Rauni", 200), ("Paavo", 100)]
    with open(file, "w", encoding="utf-8") as scores:
        for item in default_values:
            scores.write(f"{item[0]}:{item[1]}\n")


if __name__ == "__main__":
    reset_highscore()
