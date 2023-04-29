import pygame
from load_image import load_image


class Floor(pygame.sprite.Sprite):
    """ The background object where the worm can move around.

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
            x_coordinate (int, optional): The x-coordinate of the sprite. Defaults to 0.
            y_coordinate (int, optional): The y-coordinate of the sprite. Defaults to 0.
        """
        super().__init__()

        self.image = load_image("floor.png")

        self.rect = self.image.get_rect()
        self.rect.x = x_coordinate
        self.rect.y = y_coordinate
