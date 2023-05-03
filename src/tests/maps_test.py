import unittest

from game.maps import Maps


class TestHighscore(unittest.TestCase):
    def setUp(self):
        self.maps = Maps()
        self.test_map =  [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
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
        
        self.test_map_2 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                           [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                           [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                           [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                           [1, 0, 0, 0, 0, 0, 4, 0, 0, 0, 2, 0, 1],
                           [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                           [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                           [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                           [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    def test_default_map_ok(self):     
        for i in range (len(self.test_map)):
            self.assertEqual(self.test_map[i], self.maps.level_one[i])

    def test_wrong_format_map_defaults_to_test_map(self):        
        downloaded_map = self.maps.read_csv_from_url("https://drive.google.com/file/d/1toU5N30orywKx76VqoPSBdQ_0QeVhPfF/view?usp=sharing")
        self.assertEqual(self.test_map, downloaded_map)

    def test_right_format_map_downloads_okay(self):
        downloaded_map = self.maps.read_csv_from_url("https://drive.google.com/file/d/1t6NEqkcB8uRtSL4IufHtU6iH1ZQ8sHLO/view?usp=sharing")
        self.assertEqual(self.test_map_2, downloaded_map)