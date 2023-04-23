import pygame


class Renderer:
    def __init__(self, display, level):
        self._display = display
        self._level = level

    def render(self):
        pygame.display.set_caption(f"Points: {self._level.points}")        
        self._level.all_sprites.draw(self._display)
        self._level.body.draw(self._display)
        pygame.display.update()
