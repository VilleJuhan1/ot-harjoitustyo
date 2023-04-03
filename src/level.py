import random
import pygame

# Most of the the code in functions __init__() and _initialize_sprites() was
# originally created in the Sokoban-game project by Kalle Ilves:
# https://github.com/ohjelmistotekniikka-hy/pygame-sokoban

from sprites.floor import Floor
from sprites.wall import Wall
from sprites.worm import Worm
#from sprites.body import Body
from sprites.apple import Apple


class Level:
    def __init__(self, level_map, cell_size):
        self.cell_size = cell_size
        self.walls = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.worm = None
        self.apple = None
        self.body = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self._initialize_sprites(level_map)
        self.worm_direction = "L"

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
            # Try later switching 50 to self.cell_size or something related to map.
            self.worm.rect.move_ip(-50, 0)
        if self.worm_direction == "R":
            self.worm.rect.move_ip(50, 0)
        if self.worm_direction == "U":
            self.worm.rect.move_ip(0, -50)
        if self.worm_direction == "D":
            self.worm.rect.move_ip(0, 50)

    # For the time being, the new position is hard coded. Later should be able to
    # adjust to level map.
    def _apple_eaten(self):
        positions_x = [50, 100, 150, 200, 250, 300, 350, 400,
                       450, 500, 550, 600, 650, 700, 750, 800, 850, 900]
        positions_y = [50, 100, 150, 200, 250, 300, 350, 400, 450]
        self.apple.rect.update(
            (random.choice(positions_x), random.choice(positions_y)), (50, 50))
