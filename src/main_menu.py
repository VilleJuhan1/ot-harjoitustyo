import pygame
from sprites.apple import Apple

def main():

    # Need to work on the structure later, now just trying to get it work
    pygame.init()

    screen_width = 600
    screen_height = 800

    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    font = pygame.font.Font("freesansbold.ttf", 50)
    cursor_group = pygame.sprite.Group()

    pygame.display.set_caption("Snek")


    apple = Apple(screen_width // 6, (screen_height - 200) // 2 - 28)
    cursor_group.add(apple)

    choice = 1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN: # pylint: disable=no-member
                if event.key == pygame.K_DOWN: # pylint: disable=no-member
                    if choice < 3:
                        choice += 1
                if event.key == pygame.K_UP: # pylint: disable=no-member
                    if choice > 1:
                        choice -= 1
                if event.key == pygame.K_KP_ENTER: # pylint: disable=no-member
                    pass
            if event.type == pygame.QUIT:
                exit()

        screen.fill((153, 193, 241))

        new_game = font.render("New Game", True, (255,255,255))
        new_GameRect = new_game.get_rect()
        new_GameRect.center = (screen_width // 2, (screen_height - 200) // 2)
        screen.blit(new_game, new_GameRect)

        high_score = font.render("High Score", True, (255,255,255))
        high_scoreRect = high_score.get_rect()
        high_scoreRect.center = (screen_width // 2, screen_height // 2)
        screen.blit(high_score, high_scoreRect)

        exit_game = font.render("Exit Game", True, (255,255,255))
        exit_gameRect = exit_game.get_rect()
        exit_gameRect.center = (screen_width // 2, (screen_height + 200) // 2)
        screen.blit(exit_game, exit_gameRect)

        if choice == 1:
            apple.rect.update((screen_width // 6, (screen_height - 200) // 2 - 28), (50, 50))
        elif choice == 2:
            apple.rect.update((screen_width // 6, (screen_height) // 2 - 28), (50, 50))   
        elif choice == 3:
            apple.rect.update((screen_width // 6, (screen_height + 200) // 2 - 28), (50, 50))                      

        cursor_group.draw(screen)
        pygame.display.set_caption(f"Snek: {choice}")
        pygame.display.update()

        clock.tick(60)

if __name__ == "__main__":
    main()
