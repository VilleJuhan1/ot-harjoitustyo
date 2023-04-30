import unittest

from game.devcommands import Devcommands


class TestHighscore(unittest.TestCase):
    def setUp(self):
        self.dev = Devcommands()

    def test_initializes_properly(self):
        self.assertEqual("mode" in self.dev.commands.keys(), True)

    def test_false_url_not_working(self):
        test_url = "https://www.linkedin.com/in/ville-juhani-nivasalo/"
        self.assertEqual(self.dev.test_url(test_url), False)
