import pygame
from load_image import load_image


class Worm(pygame.sprite.Sprite):
    def __init__(self, x_coordinate=0, y_coordinate=0):
        super().__init__()

        self.image = load_image("head.png")
        self.rect = self.image.get_rect()
        self.rect.x = x_coordinate
        self.rect.y = y_coordinate
        self.previous_move_time = 0

    def should_move(self, current_time):
        return current_time - self.previous_move_time >= 500
