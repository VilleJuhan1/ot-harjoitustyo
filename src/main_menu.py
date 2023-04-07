import pygame

pygame.init()

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
pygame.display.set_caption("Snek")

font = pygame.font.Font("freesansbold.ttf", 40)
new_game = font.render("New Game", True, (255,255,255))
new_GameRect = new_game.get_rect()
new_GameRect.center = (800 // 2, 800 // 2)

screen.fill((153, 193, 241))
choice = 1

screen.blit(new_game, new_GameRect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: # pylint: disable=no-member
            if event.key == pygame.K_DOWN: # pylint: disable=no-member
                if choice <= 2:
                    choice += 1
            if event.key == pygame.K_UP: # pylint: disable=no-member
                if choice > 1:
                    choice -= 1
            if event.key == pygame.K_KP_ENTER: # pylint: disable=no-member
                pass
        if event.type == pygame.QUIT:
            exit()

    pygame.display.flip()
    clock.tick(60)
