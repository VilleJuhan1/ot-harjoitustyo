# The map objects need to adhere to 650 x 850 pixel display size.
# Thus the maximum width is 13 and height 17 for now.

import csv
import urllib.request
from game.devcommands import Devcommands


class Maps:
    """Maps-object handles the different tables used to render the level.

    Numbers reflect the objects in game as following:

    0. Floor
    1. Wall
    2. Worm head
    4. Apple

    Attributes:
        level_one = A table of the first playable map
    """

    def __init__(self):
        """Constructs a pool of maps usable by the game
        """
        self.level_one = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                          [1, 0, 0, 0, 0, 0, 4, 0, 0, 0, 2, 0, 1],
                          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

        self.devcommands = Devcommands()

        if self.devcommands.commands["mode"] == "online":
            self.level_two = self.read_csv_from_url(
                self.devcommands.commands["url"])

    def read_csv_from_url(self, url):  # pylint: disable=too-many-statements
        """ Reads map parameters from a .csv file in a Google drive URL.

        Checks if the parameters match the requirements, if not defaults to self.level_one

        Raises:
            ValueError: Couldn't convert str to int.

        Returns:
            list: A table containing required information for building a map.
        """
        try:
            file_id = url.split('/')[-2]
            download_url = 'https://drive.google.com/uc?export=download&id=' + file_id
            response = urllib.request.urlopen(  # pylint: disable=consider-using-with
                download_url)
            lines = [l.decode('utf-8') for l in response.readlines()]
            imported_file = csv.reader(lines)
        except Exception:  # pylint: disable=broad-exception-caught
            print("The level couldn't be loaded for some reason.")
            return self.level_one

        level_map = []

        for row in imported_file:  # pylint: disable=too-many-nested-blocks
            temp_row = []
            for value in row:
                try:
                    temp_row.append(int(value))
                    if int(value) not in [0, 1, 2, 4]:
                        print("Only numbers 0, 1, 2 and 4 allowed in maps.")
                        return self.level_one
                except Exception:
                    raise ValueError(  # pylint: disable=raise-missing-from
                        "Couln't convert the value to an integer.")
            if len(row) == len(self.level_one[0]):
                level_map.append(temp_row)
            else:
                return self.level_one

        if len(level_map) == len(self.level_one):
            return level_map

        print("The .csv file didn't match the assumed table length.")
        return self.level_one

    def return_map(self):
        """ Returns the map table

        Returns:
            list: A 2-dimensional table used for creating the game level.
        """
        if self.devcommands.commands["mode"] == "online":
            return self.level_two
        return self.level_one


if __name__ == "__main__":
    test = Maps()
