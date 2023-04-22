import unittest
import pygame

from main_menu import Menu


class TestMenu(unittest.TestCase):
    def setUp(self):
        self.menu = Menu(pygame.display.set_mode((650, 800)))

    def test_cursor_correct_starting_place(self):
        self.assertEqual(self.menu.choice, 1)
