import pygame


class Renderer:
    """Handles updating the screen inside the gameplay loop.

    Attributes:
        _display = The parameters of the displayable space in the program
        _level = A Level-object containing information and functions of the events in game

    """

    def __init__(self, display, level):
        """Constructs the Renderer-object

        Args:
            display (pygame.display): Display size is decided in the index.py
            level (Level): Level-type object
        """
        self._display = display
        self._level = level

    def render(self):
        """Updates the screen to reflect the currect game situation.

        """
        pygame.display.set_caption(f"Points: {self._level.points}")
        self._level.all_sprites.draw(self._display)
        self._level.body.draw(self._display)
        pygame.display.update()

    def render_user_input(self, text_sprites):
        pygame.display.set_caption("Game over!")
        self._level.all_sprites.draw(self._display)
        self._level.body.draw(self._display)
        pos = text_sprites[0].get_rect(center=(650/2, 300))
        self._display.blit(text_sprites[0], pos)
        pos = text_sprites[1].get_rect(center=(650/2, 400))
        self._display.blit(text_sprites[1], pos)
        pygame.display.update()
