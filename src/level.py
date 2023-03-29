import pygame
from sprites.floor import Floor
from sprites.wall import Wall
from sprites.worm import Worm
from sprites.body import Body
#from sprites.apple import Apple

class Level:
    def __init__(self, level_map, cell_size):
        self.cell_size = cell_size
        self.walls = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.worm = None
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
                    self.worm = Worm(normalized_x, normalized_y)
                    self.floors.add(Floor(normalized_x, normalized_y))
                elif cell == 3:
                    self.body.add(Body(normalized_x, normalized_y))

        self.all_sprites.add(
            self.floors,
            self.walls,
            self.worm,
            self.body
        )

    def update(self, current_time):
        if self.worm.should_move:
            self._move_worm()
        if pygame.sprite.spritecollide(self.worm, self.walls, False):
            return True

    def _move_worm(self):
        if self.worm_direction == "L":
            self.worm.rect.move_ip(-50, 0)
        if self.worm_direction == "R":
            self.worm.rect.move_ip(50, 0)
        if self.worm_direction == "U":
            self.worm.rect.move_ip(0, -50)
        if self.worm_direction == "D":
            self.worm.rect.move_ip(0, 50)

