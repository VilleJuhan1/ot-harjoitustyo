import pygame
from menu.highscore import Highscore

# The way GameLoop-class initializes and forms around other files in the
# program was originally created by Kalle Ilves in Sokoban-game project:
# https://github.com/ohjelmistotekniikka-hy/pygame-sokoban


class GameLoop:
    def __init__(self, level, renderer, event_queue, clock, cell_size):
        self._level = level
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._cell_size = cell_size
        self._highscore = Highscore()

    def start(self):
        while True:
            if self._handle_events() is False:
                break

            current_time = self._clock.get_ticks()

            collision = self._level.update(current_time)
            if collision:
                self._highscore.write_file(
                    "src/menu/scores.txt", "Player", self._level.points)
                break

            self._render()
            self._clock.tick(5)

    def _handle_events(self):  # pylint: disable=inconsistent-return-statements
        for event in self._event_queue.get():
            if event.type == pygame.KEYDOWN:  # pylint: disable=no-member
                if event.key == pygame.K_LEFT:  # pylint: disable=no-member
                    self._level.worm_direction = "L"
                if event.key == pygame.K_RIGHT:  # pylint: disable=no-member
                    self._level.worm_direction = "R"
                if event.key == pygame.K_UP:  # pylint: disable=no-member
                    self._level.worm_direction = "U"
                if event.key == pygame.K_DOWN:  # pylint: disable=no-member
                    self._level.worm_direction = "D"
                if event.key == pygame.K_ESCAPE:  # pylint: disable=no-member
                    return False
            elif event.type == pygame.QUIT:  # pylint: disable=no-member
                return False

    def _render(self):
        self._renderer.render()
