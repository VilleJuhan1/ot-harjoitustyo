import pygame
import sys

pygame.init()


class HighscoreInput:
    def __init__(self, renderer):
        self.font = pygame.font.Font("freesansbold.ttf", 50)
        self.clock = pygame.time.Clock()
        self.title_rect = self.font.render(
            "Enter name:", True, (255, 255, 255))
        self.user_input = ""
        self.renderer = renderer

    def input_player_name(self):
        loop = True
        while loop == True:

            loop = self.events()
            input_rect = self.font.render(
                self.user_input, True, (255, 255, 255))
            self.renderer.render_user_input([self.title_rect, input_rect])
            self.clock.tick(60)

        return self.user_input

    def events(self):
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


if __name__ == "__main__":
    display = pygame.display.set_mode((650, 800))
