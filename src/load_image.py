import os
import pygame


dirname = os.path.dirname(__file__)


def load_image(filename):
    """ Used in loading the images for different sprites.

    Args:
        filename (str): The filename and path for the image file

    Returns:
        pygame.image: Image object that pygame module understands.
    """
    return pygame.image.load(
        os.path.join(dirname, "assets", filename)
    )
