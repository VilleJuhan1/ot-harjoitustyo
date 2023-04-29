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


def main():
    """ Constructs the required objects and loops between menu and game.

    Doesn't contain the exit() in itself because that can be done both in menu and in-game.

    Attributes:
        maps: Imports the playable maps (2-dimension tables) from Maps class.
        level_map: The map used in the game currently.
        screen_proportions: A tuple containing the display window size in pixels.
        screen: A pygame display
        menu = Menu-class object containing the code for the main menu.
        level = Level-class object containing the code for a single game session.
        event_queue = EventQueue-class object for keeping track of the events such as 
                      button presses.
        renderer = Renderer-class object for rendering and updating the display.
        clock = A Clock-class object for keeping track of time (ticks).
        game_loop = GameLoop-class object containing the loop for a single game.

    """
    maps = Maps()
    level_map = maps.level_two
    screen_proportions = (650, 850)
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
