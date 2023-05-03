import unittest

from game.devcommands import Devcommands


class TestHighscore(unittest.TestCase):
    def setUp(self):
        self.dev = Devcommands("test", "src/tests/test_devcommands.txt")

    def test_initializes_properly(self):
        self.assertEqual("mode" in self.dev.commands.keys(), True)

    def test_false_url_not_working(self):
        test_url = "https://www.linkedin.com/in/ville-juhani-nivasalo/"
        self.assertEqual(self.dev.test_url(test_url), False)

    def test_return_values_ok(self):
        self.assertEqual(self.dev.offline_or_online(), "offline")
        self.assertEqual(self.dev.return_map_url(
        ), "https://drive.google.com/file/d/1ZsHfubrB7LQwKMvhbGr_UNvfk_GHJcix/view?usp=share_link")
