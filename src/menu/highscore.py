import sys
import pygame


test_screen = pygame.display.set_mode((650, 800))


class Highscore:
    """ The class that operates the highscore table.

    Attributes:
        scores: The five top scores in a list containing tuples, ie. ("Matti",500).
        screen: The window where score is displayed
        screen_proportions: The dimensions of the window.
        clock: pygame.time module Clock object to iterate for events and display updates.
        font: pygame.font module Font object for writing the scores.
    """

    def __init__(self, screen=test_screen, width=650, height=800):
        """ Constructor of the Highscore-object

        Args:
            screen (pygame.display, optional): The window to display. Defaults to test_screen.
            width (int, optional): Width of the screen. Defaults to 650.
            height (int, optional): Height of the screen. Defaults to 800.

        Default values are used only in testing.

        """
        pygame.init()  # pylint: disable=no-member
        self.scores = self.read_file()
        self.screen = screen
        self.screen_proportions = (width, height)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("freesansbold.ttf", 50)
        self.create_sprites(width, height)

    def read_file(self, file_name="src/menu/scores.txt"):
        """ Reads the highest scores from a text file.

        Args:
            file_name (str, optional): The file that contains the highscores. 
                                       Defaults to "src/menu/scores.txt".

        Returns:
            list: A list of tuples with the highscores.
                  One tuple contains name and score, ie. ("Matti",500).
        """
        highscore_list = []
        with open(file_name, "r", encoding="utf-8") as file:
            for line in file:
                line = line.split(":")
                name = line[0]
                score = line[1].split()[0]
                highscore_list.append((name, int(score)))

        return highscore_list

    def lowest(self):
        return self.scores[-1][1]

    def write_file(self, file_name: str, player="Tester", score=350):
        """ Saves the scores back to the file containing them. 

        Drops the worst score when writing the file.

        Args:
            file_name (str): The path where the score file is located
            player (str, optional): Name of the current player. Defaults to "Tester".
            score (int, optional): The score achieved in the current game. Defaults to 350.

        Default values are used only in testing.

        """
        self.scores.append((player, score))
        self.scores.sort(key=lambda i: i[1], reverse=True)
        with open(file_name, "w", encoding="utf-8") as file:
            for item in self.scores[:5]:
                file.write(f"{item[0]}:{item[1]}\n")

    def create_sprites(self, screen_width=650, screen_height=800):
        """ Creates the text sprites to be rendered on screen when in highscore screen.

        Args:
            screen_width (int, optional): The display width. Defaults to 650.
            screen_height (int, optional): The display height. Defaults to 800.
        """
        self.header = self.font.render(
            "Most competent worms", True, (255, 255, 255))
        self.header_rect = self.header.get_rect()
        self.header_rect.center = (
            screen_width // 2, (screen_height - 600) // 2)

        self.first_player = self.font.render(
            f"1. {self.scores[0][0]}", True, (255, 255, 255))
        self.first_score = self.font.render(
            f"{self.scores[0][1]}", True, (255, 255, 255))
        self.second_player = self.font.render(
            f"2. {self.scores[1][0]}", True, (255, 255, 255))
        self.second_score = self.font.render(
            f"{self.scores[1][1]}", True, (255, 255, 255))
        self.third_player = self.font.render(
            f"3. {self.scores[2][0]}", True, (255, 255, 255))
        self.third_score = self.font.render(
            f"{self.scores[2][1]}", True, (255, 255, 255))
        self.fourth_player = self.font.render(
            f"4. {self.scores[3][0]}", True, (255, 255, 255))
        self.fourth_score = self.font.render(
            f"{self.scores[3][1]}", True, (255, 255, 255))
        self.fifth_player = self.font.render(
            f"5. {self.scores[4][0]}", True, (255, 255, 255))
        self.fifth_score = self.font.render(
            f"{self.scores[4][1]}", True, (255, 255, 255))

    def show(self, go_back=True):
        """ This function is called when user enters the highscore from main menu.

        It is used to display the high scores.

        User can break the loop by pressing any key.

        """
        while True:
            self.render()
            if go_back is not False:
                go_back = self.get_events()
            if go_back is False:
                break
            self.clock.tick(60)

    def render(self):
        """ Renders the text sprites on screen.

        Because the scoreboard is in table form, both player name and score are rendered
        separately.

        """
        relative_x = self.screen_proportions[0] // 6
        relative_y = self.screen_proportions[1] // 4

        pygame.display.set_caption("Scoreboard")
        self.screen.fill((153, 193, 241))
        self.screen.blit(self.header, self.header_rect)
        self.screen.blit(self.first_player, (relative_x, relative_y))
        self.screen.blit(self.second_player, (relative_x, 1.5 * relative_y))
        self.screen.blit(self.third_player, (relative_x, 2 * relative_y))
        self.screen.blit(self.fourth_player, (relative_x, 2.5 * relative_y))
        self.screen.blit(self.fifth_player, (relative_x, 3 * relative_y))
        self.screen.blit(self.first_score, (relative_x * 5 -
                         self.first_score.get_width(), relative_y))
        self.screen.blit(self.second_score, (relative_x * 5 -
                         self.second_score.get_width(), 1.5 * relative_y))
        self.screen.blit(self.third_score, (relative_x * 5 -
                         self.third_score.get_width(), 2 * relative_y))
        self.screen.blit(self.fourth_score, (relative_x * 5 -
                         self.fourth_score.get_width(), 2.5 * relative_y))
        self.screen.blit(self.fifth_score, (relative_x * 5 -
                         self.fifth_score.get_width(), 3 * relative_y))
        pygame.display.update()

    def get_events(self):
        """ While on highscore menu, user can break the loop by pressing any key.

        The KEYDOWN-event is observed in this function.

        Returns:
            bool: If any key is pressed, returns False to break the loop in self.show()
        """
        for event in pygame.event.get():  # pylint: disable=too-many-nested-blocks
            if event.type == pygame.KEYDOWN:  # pylint: disable=no-member
                return False  # pylint: disable=inconsistent-return-statements
            if event.type == pygame.QUIT:  # pylint: disable=no-member
                sys.exit()
        return True


if __name__ == "__main__":
    test = Highscore()
    test.show()
