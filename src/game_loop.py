import pygame

class GameLoop:
    def __init__(self, level, renderer, event_queue, clock, cell_size):
        self._level = level
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._cell_size = cell_size

    def start(self):
        while True:
            if self._handle_events() == False:
                break

            current_time = self._clock.get_ticks()

            collision = self._level.update(current_time)
            if collision:
                break

            self._render()
            self._clock.tick(5)

    def _handle_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._level.worm_direction = "L"
                if event.key == pygame.K_RIGHT:
                    self._level.worm_direction = "R"
                if event.key == pygame.K_UP:
                    self._level.worm_direction = "U"
                if event.key == pygame.K_DOWN:
                    self._level.worm_direction = "D"
                if event.key == pygame.K_ESCAPE:
                    return False
            elif event.type == pygame.QUIT:
                return False

    def _render(self):
        self._renderer.render()
