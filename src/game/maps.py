# The map objects need to adhere to 650 x 800 pixel display size
# Thus the maximum width is 13 and height 16 for now

import csv, urllib.request

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

        self.level_two = self.read_csv_from_url()

    # This function needs some error detection
    def read_csv_from_url(self):
        url = "https://drive.google.com/file/d/1ZsHfubrB7LQwKMvhbGr_UNvfk_GHJcix/view?usp=share_link"
        file_id = url.split('/')[-2]
        download_url='https://drive.google.com/uc?export=download&id=' + file_id
        response = urllib.request.urlopen(download_url)
        lines = [l.decode('utf-8') for l in response.readlines()]
        cr = csv.reader(lines)

        level_map = []

        for row in cr:
            temp_row = []
            for value in row:
                temp_row.append(int(value))
            level_map.append(temp_row)

        return level_map

    def return_map(self):
        pass

if __name__ == "__main__":
    test = Maps()