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
    """Handles the sprites, events and possible collisions in one game session.

    Attributes:
        cell_size = The width and length of one sprite in game
        x_positions = The x-coordinates where the apple can spawn
        y_positions = the y-coordinates where the apple can spawn
        walls = pygame.sprite.Group containing all Wall-objects as sprites
        floors = pygame.sprite.Group containing all Floor-objects as sprites
        body = pygame.sprite.Group containing all Body-objects of the worm as sprites
        all_sprites = pygame.sprite.Group containing all aforementioned sprite groups
        self.worm_direction = Determines the direction of the worm (L,R,U,D)
        self.body_life_time = How long a Body-object stays alive (turns/loops)
        points = Counts the points of a single game

    """

    def __init__(self, level_map, cell_size):
        """Constructs the Level-object

        Args:
            level_map (list): A table containing the initial locations of sprites
            cell_size (int): The size of a single cell in game in pixels
        """
        self.cell_size = cell_size
        self.x_positions = self._determine_possible_apple_coordinates(
            len(level_map[0]))
        self.y_positions = self._determine_possible_apple_coordinates(
            len(level_map))
        self.walls = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.body = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self._initialize_sprites(level_map)
        self.worm_direction = "L"
        self.body_life_time = 4
        self.points = 0

    def _determine_possible_apple_coordinates(self, length):
        """Counts the coordinates where the apple can spawn in current map.

        Args:
            length (int): The length of the dimensions in the table (x or y)

        Returns:
            temp_list(list): A list containing all the possible spawn spots related
            to dimension in question
        """
        temp_list = []
        for n in range(1, length-1):  # pylint: disable=invalid-name
            temp_list.append(n * self.cell_size)
        return temp_list

    def _initialize_sprites(self, level_map):
        """Goes through the level_map-table and initializes sprites accordingly.

        Adds all sprites (except body) to sprite group all_sprites.

        Args:
            level_map (Maps): A 2-dimensional table containing information on where
            to spawn different elements in the game
        """
        # pylint: disable=consider-using-enumerate

        for number_of_y in range(len(level_map)):  # pylint: disable=inconsistent-return-statements
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

        self.all_sprites.add(
            self.floors,
            self.walls,
            self.apple,
            self.worm,
        )

    def update(self, current_time):  # pylint: disable=inconsistent-return-statements
        """ This function handles the collisions, movement and later growth of the worm.

        Args:
            current_time (pygame.time.get_ticks()): How many clock ticks since the game started

        Returns:
            bool: If collision is detected with walls or body, inform GameLoop accordingly.
        """
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

    def _move_worm(self):
        """ The worm moves in the set direction after certain time has passed.

        The direction is read from the variable worm_direction (L, R, U, D).
        """
        if self.worm_direction == "L":
            self.worm.rect.move_ip(-self.cell_size, 0)
        if self.worm_direction == "R":
            self.worm.rect.move_ip(self.cell_size, 0)
        if self.worm_direction == "U":
            self.worm.rect.move_ip(0, -self.cell_size)
        if self.worm_direction == "D":
            self.worm.rect.move_ip(0, self.cell_size)

    def _spawn_body_sprite(self, x_coordinate, y_coordinate):
        """ Spawns a new body sprite every time the head moves.

        Args:
            x_coordinate (int): x-coordinate for the new Body-sprite
            y_coordinate (int): y-coordinate for the new Body-sprite
        """
        self.body.add(Body(self.body_life_time, x_coordinate, y_coordinate))

    def _kill_last_sprite(self):
        """ Effectively reduces the life of all body sprites by 1. t

        Once the time to live hits 0, the sprite is killed.

        If an apple is eaten, this function is skipped.
        """
        for sprite in self.body:
            sprite.lifetime -= 1
            if sprite.lifetime == 0:
                sprite.kill()

    def _apple_eaten(self):
        """ The Apple is spawned inside the arena, but not inside the worm.

        """
        self.points += 10
        while True:
            self.apple.rect.update(
                (random.choice(self.x_positions), random.choice(self.y_positions)), (50, 50))
            if not pygame.sprite.spritecollide(self.apple, self.body, False):
                if not pygame.sprite.spritecollide(self.apple, self.walls, False):
                    break

        self.body_life_time += 1
