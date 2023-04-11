import pygame

# The basic functionality of the program in the main()-function was originally created
# by Kalle Ilves for Sokoban-game project: https://github.com/ohjelmistotekniikka-hy/pygame-sokoban

from game.level import Level
from game.game_loop import GameLoop
from game.event_queue import EventQueue
from game.renderer import Renderer
from game.clock import Clock
from game.maps import Maps
from main_menu import Menu

CELL_SIZE = 50

# The menu functionality doesn't include high scores at the moment. However it does allow the user
# to start a new game over and over or quit game all together.


def main():
    maps = Maps()
    level_map = maps.level_one
    screen_proportions = (650, 800)
    screen = pygame.display.set_mode(screen_proportions)

    while True:

        # Quitting pygame-object and closing the game can be done in menu
        menu = Menu(screen)
        menu.loop()

        # Game loop needs a reset before every game because the parameters differ
        # from menu apart from screen size and title
        level = Level(level_map, CELL_SIZE)
        event_queue = EventQueue()
        renderer = Renderer(screen, level)
        clock = Clock()
        game_loop = GameLoop(level, renderer, event_queue, clock, CELL_SIZE)
        game_loop.start()


if __name__ == "__main__":
    main()
