import pygame


class Clock:
    """Works as a timer for both the speed of the worm and fps of the game.

    Attributes:
        ._clock = A Clock-object from pygame.time module.
    """

    def __init__(self):
        """The constructor to create a new Clock-object.

        """
        self._clock = pygame.time.Clock()

    def tick(self, fps):
        """Controls the speed how often the clock ticks in a second

        Args:
            fps (int): Refresh rate in frames per second
        """
        self._clock.tick(fps)

    def get_ticks(self):
        """Returns the amount of clock ticks that have happened so far

        Returns:
            pygame.time module function get_ticks()
        """
        return pygame.time.get_ticks()
