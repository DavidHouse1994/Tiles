import pygame, sys, os
from pygame.locals import *

clock = pygame.time.Clock()

pygame.display.set_caption("Pygame window")

WINDOW_SIZE = (400, 400)

pygame.init()

player = pygame.image.load('player.png')

player_location = [40, 40]
moving_right = False
moving_left = False

player_y_momentum = 0

player_rect = pygame.Rect(player_location[0], player_location[1], player.get_width(), player.get_height())
test_rect = pygame.Rect(100, 100, 100, 50)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

while True:
    screen.fill((0, 0, 0))
    screen.blit(player, player_location)
    
    if player_location[1] > WINDOW_SIZE[1]-player.get_height():
        player_y_momentum = -player_y_momentum
    else:
        player_y_momentum += 0.2
    player_location[1] += player_y_momentum
    
    if moving_right:
        player_location[0] += 4
    if moving_left:
        player_location[0] -= 4
        
    player_rect.x = player_location[0]
    player_rect.y = player_location[1]
    
    if player_rect.colliderect(test_rect):
        pygame.draw.rect(screen, (255, 0, 0), test_rect)
    else:
        pygame.draw.rect(screen, (0, 255, 0), test_rect)
        
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False
        

    pygame.display.update()
    clock.tick(60)
