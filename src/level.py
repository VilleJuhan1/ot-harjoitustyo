import random
import pygame

# The original code in functions __init__() and _initialize_sprites() 
# was created in the Sokoban-game project by Kalle Ilves:
# https://github.com/ohjelmistotekniikka-hy/pygame-sokoban

from sprites.floor import Floor
from sprites.wall import Wall
from sprites.worm import Worm
#from sprites.body import Body
from sprites.apple import Apple


class Level:
    def __init__(self, level_map, cell_size, height, width):
        self.cell_size = cell_size
        self.x_positions = self._determine_possible_apple_coordinates(width)
        self.y_positions = self._determine_possible_apple_coordinates(height)
        self.walls = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.worm = None
        self.apple = None
        self.body = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self._initialize_sprites(level_map)
        self.worm_direction = "L"

    def _determine_possible_apple_coordinates(self, width):
        list = []
        for n in range(1, width-1):
            list.append(n * self.cell_size)
        return list

    def _initialize_sprites(self, level_map):
        height = len(level_map)
        width = len(level_map[0])

        for number_of_y in range(height):
            for number_of_x in range(width):
                cell = level_map[number_of_y][number_of_x]
                normalized_x = number_of_x * self.cell_size
                normalized_y = number_of_y * self.cell_size

                if cell == 0:
                    self.floors.add(Floor(normalized_x, normalized_y))
                elif cell == 1:
                    self.walls.add(Wall(normalized_x, normalized_y))
                elif cell == 2:
                    self.worm = Worm(normalized_x, normalized_y)
                    self.floors.add(Floor(normalized_x, normalized_y))
                # elif cell == 3:
                #    self.body.add(Body(normalized_x, normalized_y))
                elif cell == 4:
                    self.apple = Apple(normalized_x, normalized_y)
                    self.floors.add(Floor(normalized_x, normalized_y))

        self.all_sprites.add(
            self.floors,
            self.walls,
            self.apple,
            self.worm,
            # self.body
        )

    # This function handles the collisions, movement and later growth of the worm.
    def update(self, current_time): # pylint: disable=inconsistent-return-statements
        if self.worm.should_move(current_time):
            self._move_worm()
        if pygame.sprite.spritecollide(self.worm, self.walls, False):
            return True
        if self.worm.rect.colliderect(self.apple.rect):
            self._apple_eaten()

    # Worm moves in the set direction after certain time has passed, the direction
    # is stored in worm_direction.
    def _move_worm(self):
        if self.worm_direction == "L":
            self.worm.rect.move_ip(-self.cell_size, 0)
        if self.worm_direction == "R":
            self.worm.rect.move_ip(self.cell_size, 0)
        if self.worm_direction == "U":
            self.worm.rect.move_ip(0, -self.cell_size)
        if self.worm_direction == "D":
            self.worm.rect.move_ip(0, self.cell_size)

    # The apple spawns randomly inside the arena on every map
    def _apple_eaten(self):
        self.apple.rect.update(
            (random.choice(self.x_positions), random.choice(self.y_positions)), (50, 50))
