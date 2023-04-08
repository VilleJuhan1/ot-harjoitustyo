import pygame

# The basic functionality of the program in the game()-function was originally created
# by Kalle Ilves for Sokoban-game project: https://github.com/ohjelmistotekniikka-hy/pygame-sokoban

from game.level import Level
from game.game_loop import GameLoop
from game.event_queue import EventQueue
from game.renderer import Renderer
from game.clock import Clock
from game.maps import Maps
from user_interface.main_menu import Menu

CELL_SIZE = 50

# The menu functionality doesn't include high scores at the moment. However it does allow the user
# to start a new game over and over or quit game all together.


def main():
    while True:
        menu = Menu()
        menu.loop()
        game()


def game():
    maps = Maps()
    level_map = maps.level_one
    height = len(level_map)
    width = len(level_map[0])
    display_height = height * CELL_SIZE
    display_width = width * CELL_SIZE
    display = pygame.display.set_mode((display_width, display_height))

    pygame.display.set_caption("Snek")

    level = Level(level_map, CELL_SIZE)
    event_queue = EventQueue()
    renderer = Renderer(display, level)
    clock = Clock()
    game_loop = GameLoop(level, renderer, event_queue, clock, CELL_SIZE)

    pygame.init()  # pylint: disable=no-member
    game_loop.start()


if __name__ == "__main__":
    main()
