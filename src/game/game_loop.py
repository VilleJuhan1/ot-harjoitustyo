import pygame
from menu.highscore import Highscore
from menu.highscore_input import HighscoreInput

# The way GameLoop-class initializes and forms around other files in the
# program was originally created by Kalle Ilves in Sokoban-game project:
# https://github.com/ohjelmistotekniikka-hy/pygame-sokoban


class GameLoop:
    """Contains the loop for the gameplay part of the program.

    The events in the game are in the module Level.

    Attributes:
        _level = The level where the "action" happens
        _renderer = The object that handles updating the screen
        _event_queue = The object that handles pygame events such as KEY.DOWN
        _clock = The pygame object that handles passed time and ticks
        _cell_size = The size of one cell in the game map
        _highscore = The object that handles the scoreboard

    """

    def __init__(self, level, renderer, event_queue, clock, cell_size):
        """Constructor of the GameLoop-object

        Args:
            level (Level)
            renderer (Renderer)
            event_queue (EventQueue)
            clock (Clock)
            cell_size (int): The width and length of one object in the game map
        """
        self._level = level
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._cell_size = cell_size
        self._highscore = Highscore()
        self._user_input = HighscoreInput(self._renderer)

    def start(self):
        """Handles the loop which runs one game session from start to finish.

        The loop is broken on two conditions:

        1. Player presses ESCAPE-button which terminates the current game immediately.
        2. The worm collides with itself or a Wall-object

        """
        while True:
            if self._handle_events() is False:
                break

            current_time = self._clock.get_ticks()

            collision = self._level.update(current_time)
            if collision:
                if self._level.points > self._highscore.lowest():
                    self._highscore.write_file(
                        "src/menu/scores.txt",
                        self._user_input.input_player_name(),
                        self._level.points)
                break

            self._render()
            self._clock.tick(5)

    def _handle_events(self):
        """Keeps track of the button presses.

        Changes the direction of the worm when arrow keys are pressed.

        Returns:
            bool: Returns false if the player exits the game or presses ESCAPE-button
        """
        for event in self._event_queue.get():
            if event.type == pygame.KEYDOWN:  # pylint: disable=no-member
                if event.key == pygame.K_LEFT:  # pylint: disable=no-member
                    self._level.worm_direction = "L"
                if event.key == pygame.K_RIGHT:  # pylint: disable=no-member
                    self._level.worm_direction = "R"
                if event.key == pygame.K_UP:  # pylint: disable=no-member
                    self._level.worm_direction = "U"
                if event.key == pygame.K_DOWN:  # pylint: disable=no-member
                    self._level.worm_direction = "D"
                if event.key == pygame.K_ESCAPE:  # pylint: disable=no-member
                    return False
            elif event.type == pygame.QUIT:  # pylint: disable=no-member
                return False

        return True

    def _render(self):
        """Renders the screen to reflect the updates in the game.
        """
        self._renderer.render()
