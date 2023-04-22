import random
import pygame

# The original code in functions __init__() and _initialize_sprites()
# was created in the Sokoban-game project by Kalle Ilves:
# https://github.com/ohjelmistotekniikka-hy/pygame-sokoban

from sprites.floor import Floor
from sprites.wall import Wall
from sprites.worm import Worm
from sprites.body import Body
from sprites.apple import Apple


class Level:
    # Too many instance attributes here, work on it.
    def __init__(self, level_map, cell_size):
        self.cell_size = cell_size
        self.x_positions = self._determine_possible_apple_coordinates(
            len(level_map[0]))
        self.y_positions = self._determine_possible_apple_coordinates(
            len(level_map))
        self.walls = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        # self.worm = None
        # self.apple = None
        self.body = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self._initialize_sprites(level_map)
        self.worm_direction = "L"
        self.body_life_time = 4

    def _determine_possible_apple_coordinates(self, length):
        temp_list = []
        for n in range(1, length-1):  # pylint: disable=invalid-name
            temp_list.append(n * self.cell_size)
        return temp_list

    # This function initializes the chosen map (currently only one possible).
    def _initialize_sprites(self, level_map):

        for number_of_y in range(len(level_map)):
            for number_of_x in range(len(level_map[0])):
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
                elif cell == 4:
                    self.apple = Apple(normalized_x, normalized_y)
                    self.floors.add(Floor(normalized_x, normalized_y))

        # Yeah this is not all sprites because the body is handled separately, work on this.
        self.all_sprites.add(
            self.floors,
            self.walls,
            self.apple,
            self.worm,
        )

    # This function handles the collisions, movement and later growth of the worm.
    def update(self, current_time):  # pylint: disable=inconsistent-return-statements
        if self.worm.should_move(current_time):
            x_coordinate = self.worm.rect.x
            y_coordinate = self.worm.rect.y
            self._move_worm()
            self._spawn_body_sprite(x_coordinate, y_coordinate)

        if pygame.sprite.spritecollide(self.worm, self.walls, False):
            return True
        if pygame.sprite.spritecollide(self.worm, self.body, False):
            return True
        if self.worm.rect.colliderect(self.apple.rect):
            self._apple_eaten()
        else:
            self._kill_last_sprite()

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

    # This function spawns new body sprite after the head moves
    def _spawn_body_sprite(self, x_coordinate, y_coordinate):
        self.body.add(Body(self.body_life_time, x_coordinate, y_coordinate))

    # This function effectively reduces the life of all body sprites by 1 thus
    # "killing" the last one with updated lifetime of 0
    def _kill_last_sprite(self):
        for sprite in self.body:
            sprite.lifetime -= 1
            if sprite.lifetime == 0:
                sprite.kill()

    # The apple spawns randomly inside the arena on every map
    def _apple_eaten(self):
        while True:
            self.apple.rect.update(
                (random.choice(self.x_positions), random.choice(self.y_positions)), (50, 50))
            if not pygame.sprite.spritecollide(self.apple, self.body, False):
                break

        self.body_life_time += 1
