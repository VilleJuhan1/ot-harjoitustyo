import pygame
from load_image import load_image


class Body(pygame.sprite.Sprite):
    def __init__(self, life, x_coordinate, y_coordinate):
        super().__init__()

        self.image = load_image("body.png")

        self.rect = self.image.get_rect()
        self.rect.x = x_coordinate
        self.rect.y = y_coordinate
        self.lifetime = life
