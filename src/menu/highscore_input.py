import pygame

pygame.init()


class HighscoreInput:
    """ Handles the keyboard inputs if the player scores high enough to enter highscoreboard.

    Attributes:
        font: Used in rendering text sprites with pygame.
        clock: Used in counting "ticks" or updates with pygame.
        title_rect: The title that appears over the input box.
        user_input: The string that keeps track of the player input.
        renderer: Renderer-class object that is inherited from GameLoop.

    """
    def __init__(self, renderer):
        """ The constructor

        Args:
            renderer (Renderer): Inherited Renderer-class object so that the sprites are displayed in the same display
            as others.
        """
        self.font = pygame.font.Font("freesansbold.ttf", 50)
        self.clock = pygame.time.Clock()
        self.title_rect = self.font.render(
            "Enter name:", True, (255, 255, 255))
        self.user_input = ""
        self.renderer = renderer

    def input_player_name(self):
        """ Handles the events during name input process.

        Returns:
            str: The name player wants displayed on scoreboard.
        """
        loop = True
        while loop == True:

            loop = self.events()
            input_rect = self.font.render(
                self.user_input, True, (255, 255, 255))
            self.renderer.render_user_input([self.title_rect, input_rect])
            self.clock.tick(60)

        return self.user_input

    def events(self):
        """ Keeps track of keypresses.

        Returns:
            bool: If player is ready, that is affirmed with Return-key thus returning value False.
        """
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    return False
                elif event.key == pygame.K_BACKSPACE:
                    self.user_input = self.user_input[:-1]
                else:
                    if len(self.user_input) <= 8:
                        self.user_input += event.unicode

        return True

