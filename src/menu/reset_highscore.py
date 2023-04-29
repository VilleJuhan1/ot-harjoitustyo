def reset_highscore(file="src/menu/scores.txt"):
    """Resets the highscore table to default values

    Args:
        file (str, optional): The file containing highscores. Defaults to "src/menu/scores.txt".

    Calling the function with a different filename can be used in testing.

    """
    default_values = [("Mauno", 500), ("Rauno", 400),
                      ("Pauli", 300), ("Rauni", 200), ("Paavo", 100)]
    with open(file, "w", encoding="utf-8") as scores:
        for item in default_values:
            scores.write(f"{item[0]}:{item[1]}\n")


if __name__ == "__main__":
    reset_highscore()
