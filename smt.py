

import pygame
import sys
import os
from time import sleep


pygame.init()
go = True


screen = pygame.display.set_mode((1580, 1080))
pygame.draw.circle(screen, (255, 255, 0), [2, 2], 30)
image = pygame.image.load(os.path.join("stimuli_img", 'frog.png')).convert_alpha()
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

