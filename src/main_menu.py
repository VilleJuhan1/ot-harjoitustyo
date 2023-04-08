import pygame
from sprites.apple import Apple

class Menu:
    def __init__(self):
        pygame.init()
        self.screen_width = 600
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("freesansbold.ttf", 50)
        self.sprites = pygame.sprite.Group()
        self.init_sprites()
        self.choice = 1

    def init_sprites(self):
        self.apple = Apple(self.screen_width // 6, (self.screen_height - 200) // 2 - 28)
        self.sprites.add(self.apple)

        self.new_game = self.font.render("New Game", True, (255,255,255))
        self.new_GameRect = self.new_game.get_rect()
        self.new_GameRect.center = (self.screen_width // 2, (self.screen_height - 200) // 2)

        self.high_score = self.font.render("High Score", True, (255,255,255))
        self.high_scoreRect = self.high_score.get_rect()
        self.high_scoreRect.center = (self.screen_width // 2, self.screen_height // 2)

        self.exit_game = self.font.render("Exit Game", True, (255,255,255))
        self.exit_gameRect = self.exit_game.get_rect()
        self.exit_gameRect.center = (self.screen_width // 2, (self.screen_height + 200) // 2) 

    def loop(self):
        game = False
        while not game:
            self.render()
            game = self.get_events()
        return

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN: # pylint: disable=no-member
                if event.key == pygame.K_DOWN: # pylint: disable=no-member
                    if self.choice < 3:
                        self.choice += 1
                if event.key == pygame.K_UP: # pylint: disable=no-member
                    if self.choice > 1:
                        self.choice -= 1
                if event.key == pygame.K_RETURN: # pylint: disable=no-member
                    if self.choice == 1:
                        return True
                        exit()
                    elif self.choice == 2:
                        pass
                    elif self.choice == 3:
                        exit()
            if event.type == pygame.QUIT:
                exit()

    def render(self):
        pygame.display.set_caption("Snek")
        self.screen.fill((153, 193, 241))
        self.screen.blit(self.new_game, self.new_GameRect)
        self.screen.blit(self.high_score, self.high_scoreRect)
        self.screen.blit(self.exit_game, self.exit_gameRect)

        if self.choice == 1:
            self.apple.rect.update((self.screen_width // 6, (self.screen_height - 200) // 2 - 28), (50, 50))
        elif self.choice == 2:
            self.apple.rect.update((self.screen_width // 6, (self.screen_height) // 2 - 28), (50, 50))   
        elif self.choice == 3:
            self.apple.rect.update((self.screen_width // 6, (self.screen_height + 200) // 2 - 28), (50, 50))                      

        self.sprites.draw(self.screen)
        pygame.display.update()
        self.clock.tick(60)

if __name__ == "__main__":
    app = Menu()
    app.loop()
