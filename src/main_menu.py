import sys
import os
import pygame
from sprites.apple import Apple
from menu.highscore import Highscore


class Menu:
    """ The class that handles the code required for running the main menu in game.

    Attributes:
        screen: The display.
        screen_width: The display width in pixels.
        screen_height: The display height in pixels.
        clock: pygame.time.Clock()-class object to handle ticks.
        font: pygame.font.Font()-class object to be used in printing text.
        sprites: pygame.sprite.Group()-class object to handle the sprites in menu.
        choice: The variable that keeps track of the red cursor (Apple) position.
        highscore: Highscore()-class object that is used in menu to read and print highscores.

    """

    def __init__(self, screen):
        """ The constructor

        Args:
            screen (pygame.display): The window where the information is handled.
        """
        os.environ['SDL_VIDEO_WINDOW_POS'] = f"{700},{400}"
        pygame.init()  # pylint: disable=no-member
        self.screen = screen
        self.screen_width = 650
        self.screen_height = 850
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("freesansbold.ttf", 50)
        self.sprites = pygame.sprite.Group()
        self.init_sprites()
        self.choice = 1
        self.highscore = Highscore()

    def init_sprites(self):
        """ Initializes the sprites on screen.

        """
        self.apple = Apple(self.screen_width // 6,
                           (self.screen_height - 200) // 2 - 28)
        self.sprites.add(self.apple)

        self.new_game = self.font.render("New Game", True, (255, 255, 255))
        self.new_game_rect = self.new_game.get_rect()
        self.new_game_rect.center = (
            self.screen_width // 2, (self.screen_height - 200) // 2)

        self.high_score = self.font.render("High Score", True, (255, 255, 255))
        self.high_score_rect = self.high_score.get_rect()
        self.high_score_rect.center = (
            self.screen_width // 2, self.screen_height // 2)

        self.exit_game = self.font.render("Exit Game", True, (255, 255, 255))
        self.exit_game_rect = self.exit_game.get_rect()
        self.exit_game_rect.center = (
            self.screen_width // 2, (self.screen_height + 200) // 2)

    def loop(self):
        """ The menu loop when the user is in the main menu.

        Keeps track of up and down arrow key presses to change the position of the cursor.

        The loop breaks when the user chooses "New game" thus returning back to the loop
        in index.py.

        Attributes:
            chosen: User chooses a menu item by pressing enter. The variable changes accordingly.

        Args:
            is_test (bool): Can be used in testing. 
        """
        chosen = None
        while chosen != "game":
            self.render()
            chosen = self.get_events()
            if chosen == "score":
                self.highscore = Highscore(
                    self.screen, self.screen_width, self.screen_height)
                self.highscore.show()
                chosen = None

    def get_events(self):
        """ Checks for certain button presses inside the menu.

        Returns:
            str: Returns the variable that triggers an object in the menu.
        """
        for event in pygame.event.get():  # pylint: disable=too-many-nested-blocks
            if event.type == pygame.KEYDOWN:  # pylint: disable=no-member
                if event.key == pygame.K_DOWN:  # pylint: disable=no-member
                    if self.choice < 3:
                        self.choice += 1
                if event.key == pygame.K_UP:  # pylint: disable=no-member
                    if self.choice > 1:
                        self.choice -= 1
                if event.key == pygame.K_RETURN:  # pylint: disable=no-member
                    if self.choice == 1:
                        return "game"
                    if self.choice == 2:
                        return "score"
                    if self.choice == 3:
                        sys.exit()
            if event.type == pygame.QUIT:  # pylint: disable=no-member
                sys.exit()

        return None

    def render(self):
        """ Renders the initial screen and updates the position of the cursor in menu.

        """
        pygame.display.set_caption("Main menu")
        self.screen.fill((153, 193, 241))
        self.screen.blit(self.new_game, self.new_game_rect)
        self.screen.blit(self.high_score, self.high_score_rect)
        self.screen.blit(self.exit_game, self.exit_game_rect)

        if self.choice == 1:
            self.apple.rect.update(
                (self.screen_width // 6, (self.screen_height - 200) // 2 - 28), (50, 50))
        elif self.choice == 2:
            self.apple.rect.update(
                (self.screen_width // 6, (self.screen_height) // 2 - 28), (50, 50))
        elif self.choice == 3:
            self.apple.rect.update(
                (self.screen_width // 6, (self.screen_height + 200) // 2 - 28), (50, 50))

        self.sprites.draw(self.screen)
        pygame.display.update()
        self.clock.tick(60)


if __name__ == "__main__":
    app = Menu(pygame.display.set_mode((650, 800)))
    app.loop()
