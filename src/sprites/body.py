import pygame
from load_image import load_image


class Body(pygame.sprite.Sprite):
    """ The Body-sprites of the worm.

    Attributes:
        image = The 50x50 pixel image used in every type of this object.
        rect = The hitbox of the object.
        rect.x = The x-coordinate of the hitbox (upper left corner).
        rect.y = The y-coordinate of the hitbox (upper left corner).
        lifetime = How many moves (turns) the spawned sprite will live until it is "killed".        

    Args:
        pygame (Sprite): A sprite object recognized by pygame library.
    """

    def __init__(self, life, x_coordinate, y_coordinate):
        """ The constructor.

        Args:
            life (int): The amount of moves (turns) the sprite will live.
            x_coordinate (int): The body spawns always on the spot where the Worm-object last was.
            y_coordinate (int): These coordinates are delivered in the function call as x and y.
        """
        super().__init__()

        self.image = load_image("body.png")

        self.rect = self.image.get_rect()
        self.rect.x = x_coordinate
        self.rect.y = y_coordinate
        self.lifetime = life
