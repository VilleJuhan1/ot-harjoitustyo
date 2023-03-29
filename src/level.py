import pygame
from sprites.floor import Floor
from sprites.wall import Wall
from sprites.worm import Worm
from sprites.body import Body

class Level:
    def __init__(self, level_map, cell_size):
        self.cell_size = cell_size
        self.walls = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.worm = pygame.sprite.Group()
        self.body = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self._initialize_sprites(level_map)
        self.worm_direction = "L"

    def _initialize_sprites(self, level_map):
        height = len(level_map)
        width = len(level_map[0])

        for y in range(height):
            for x in range(width):
                cell = level_map[y][x]
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size

                if cell == 0:
                    self.floors.add(Floor(normalized_x, normalized_y))
                elif cell == 1:
                    self.walls.add(Wall(normalized_x, normalized_y))
                elif cell == 2:
                    self.worm.add(Worm(normalized_x, normalized_y))
                elif cell == 3:
                    self.body.add(Body(normalized_x, normalized_y))

        self.all_sprites.add(
            self.floors,
            self.walls,
            self.worm,
            self.body
        )

    def update(self, current_time):
        for worm in self.worm:
            if worm.should_move(current_time):
                self._move_worm(worm)

    def _move_worm(self, worm):
        pass
