import unittest
import pygame

from game.level import Level

LEVEL_MAP_1 = [[1, 1, 1, 1, 1],
               [1, 0, 0, 0, 1],
               [1, 0, 2, 0, 1],
               [1, 4, 0, 0, 1],
               [1, 1, 1, 1, 1]]

CELL_SIZE = 50

height = len(LEVEL_MAP_1)
width = len(LEVEL_MAP_1[0])


class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level = Level(LEVEL_MAP_1, CELL_SIZE)
        self.worm = self.level.worm

    def assert_coordinates_equal(self, sprite, x, y):
        self.assertEqual(sprite.rect.x, x)
        self.assertEqual(sprite.rect.y, y)

    def test_worm_head_is_in_the_right_starting_position(self):
        self.assert_coordinates_equal(
            self.level.worm, 2 * CELL_SIZE, 2 * CELL_SIZE)

    def test_worm_moves_left_by_default(self):
        self.level._move_worm()
        self.assert_coordinates_equal(
            self.level.worm, 1 * CELL_SIZE, 2 * CELL_SIZE)

    def test_worm_moves_up(self):
        self.level.worm_direction = "U"

        self.level._move_worm()
        self.assert_coordinates_equal(
            self.level.worm, 2 * CELL_SIZE, 1 * CELL_SIZE)

    def test_worm_moves_down(self):
        self.level.worm_direction = "D"

        self.level._move_worm()
        self.assert_coordinates_equal(
            self.level.worm, 2 * CELL_SIZE, 3 * CELL_SIZE)

    def test_worm_collides_with_apple(self):
        self.level.worm_direction = "L"
        self.level._move_worm()
        self.level.worm_direction = "D"
        self.level._move_worm()
        self.assertEqual(self.worm.rect.colliderect(
            self.level.apple.rect), True)

    def test_worm_collides_with_walls(self):
        self.level.worm_direction = "L"
        self.level._move_worm()
        self.level._move_worm()
        self.assertEqual(self.level.update(0), True)
