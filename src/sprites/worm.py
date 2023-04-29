import pygame
from load_image import load_image


class Worm(pygame.sprite.Sprite):
    """ The playable sprite that responds to keyboard commands (Worm head).

    The class holds the constructor and the timer function that checks whether the worm should move.

    The movement itself is done in the Level-object.

    Attributes:
        image = The 50x50 pixel image used in every type of this object.
        rect = The hitbox of the object.
        rect.x = The x-coordinate of the hitbox (upper left corner).
        rect.y = The y-coordinate of the hitbox (upper left corner).

    Args:
        pygame (Sprite): A sprite object recognized by pygame library.
    """

    def __init__(self, x_coordinate=0, y_coordinate=0):
        """ The constructor.

        Args:
            x_coordinate (int, optional): The spawn spot of the worm head (x). Defaults to 0.
            y_coordinate (int, optional): The spawn spot of the worm head (y). Defaults to 0.
        """
        super().__init__()

        self.image = load_image("head.png")
        self.rect = self.image.get_rect()
        self.rect.x = x_coordinate
        self.rect.y = y_coordinate
        self.previous_move_time = 0

    def should_move(self, current_time):
        return current_time - self.previous_move_time >= 500
