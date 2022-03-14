

import pygame
import sys
import os


pygame.init()
go = True


screen = pygame.display.set_mode((1580, 1080))
screen.fill((237, 211, 156))
pygame.draw.circle(screen, (255, 255, 0), [2, 2], 30)
image = pygame.image.load(os.path.join("stimuli_img", 'frog.png'))
screen.blit(image, (50, 50))


pygame.display.update()

while go is True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
