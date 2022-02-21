

"""Тут находится отслеживание работы клавиш, а также вывод информации на экран с помощью модуля PyGame"""


import pygame
import sys


'''Нижу находятся словари-расшифровщики'''

figure_dict_for_n_back = {"triangle": "", "sphere": "", "square": "",
                          "circle": "", "pyramid": "", "oval": "", "prism": ""}

color_dict_for_n_back = {"white": (255, 255, 255), "red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255),
                         "yellow": (225, 225, 0), "brown": (100, 50, 30), "black": (0, 0, 0), "orange": (255, 100, 25)}


def pygame_func():
    pygame.init()

    screen = pygame.display.set_mode((640, 480))
    rect = pygame.Rect(20, 20, 50, 70)
    color = color_dict_for_n_back["red"]
    pygame.draw.circle(screen, color_dict_for_n_back["blue"],
                       (100, 100), 50)
    pygame.draw.circle(screen, color_dict_for_n_back["green"],
                       (200, 100), 50, 10)
    pygame.draw.polygon(screen, color_dict_for_n_back["white"],
                        [[150, 10], [180, 50],
                         [90, 90], [30, 30]])
    pygame.draw.polygon(screen, color_dict_for_n_back["orange"],
                        [[250, 110], [280, 150],
                         [190, 190], [130, 130]])
    pygame.draw.aalines(screen, color_dict_for_n_back["brown"], True,
                        [[250, 110], [280, 150],
                         [190, 190], [130, 130]])

    # Обработка событий должна происходить ТОЛЬКО в цикле.
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    color = color_dict_for_n_back["black"]

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    color = color_dict_for_n_back["red"]

        pygame.draw.rect(screen, color, rect, 0)
        pygame.display.flip()


pygame_func()
