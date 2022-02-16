

"""Тут находится отслеживание работы клавишь, а также вывод информации на экран с помозью модуля PyGame"""


import pygame
import sys


def pygame_func():
    pygame.init()

    screen = pygame.display.set_mode((640, 480))
    rect = pygame.Rect(20, 20, 50, 70)
    color = (255, 255, 255)

    # Обработка событий должна происходить ТОЛЬКО в цикле. И это хорошо.
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    color = (0, 0, 0)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    color = (255, 255, 255)

        pygame.draw.rect(screen, color, rect, 0)
        pygame.display.flip()
