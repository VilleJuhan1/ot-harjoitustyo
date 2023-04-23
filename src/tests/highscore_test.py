import unittest
import pygame

from menu.highscore import Highscore
import menu.reset_highscore


class TestHighscore(unittest.TestCase):
    def setUp(self):
        self.scoreboard = Highscore()

    def test_file_read_correctly_as_tuple(self):
        self.scoreboard.scores = self.scoreboard.read_file("src/tests/test_highscore.txt")
        self.assertEqual(self.scoreboard.scores[0], ("Mauno",500))

    def test_write_file_part_one_list(self):
        self.scoreboard.write_file("src/tests/test_highscore.txt", "Jarmo", 550)
        self.scoreboard.scores = self.scoreboard.read_file("src/tests/test_highscore.txt")
        self.assertEqual(self.scoreboard.scores[0], ("Jarmo",550))

    def test_write_file_part_two_reset(self):
        menu.reset_highscore.reset_highscore("src/tests/test_highscore.txt")

    def test_write_file_part_three_default_value(self):
        self.assertEqual(self.scoreboard.scores[0], ("Mauno",500))

