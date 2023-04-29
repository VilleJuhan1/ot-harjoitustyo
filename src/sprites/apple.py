import pygame
from load_image import load_image


class Apple(pygame.sprite.Sprite):
    """ The edible in the game.

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
            x_coordinate (int, optional): Semi-randomized spawn spot of the Apple-object (x).
            y_coordinate (int, optional): Semi-randomized spawn spot of the Apple-object (y).
        """
        super().__init__()

        self.image = load_image("apple.png")

        self.rect = self.image.get_rect()
        self.rect.x = x_coordinate
        self.rect.y = y_coordinate
