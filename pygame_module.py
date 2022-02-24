

"""Тут находится отслеживание работы клавиш, а также вывод информации на экран с помощью модуля PyGame"""


import pygame
import sys


'''Нижу находятся словари-расшифровщики'''


#  Подозреваю, что словарь с фигурами тут не нужен... Или нужно как-то это переработать.
#  Может только позиционирование прописать надо? Непонятно.
figure_dict_for_n_back = {"triangle": "", "sphere": "", "square": "",
                          "circle": "", "pyramid": "", "oval": "", "prism": ""}

color_dict_for_n_back = {"white": (255, 255, 255), "red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255),
                         "yellow": (225, 225, 0), "brown": (100, 50, 30), "black": (0, 0, 0), "orange": (255, 100, 25),
                         "beige": (237, 211, 156)}


def pygame_func():

    def quit_pygame():
        pygame.quit()
        sys.exit()

    pygame.init()

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    b = type(pygame.display.get_window_size())
    a = pygame.display.get_window_size()
    print(b)
    print(a[0])
    print(a[1])

    position = [[a[0] / 2, a[1] / 2 - 150], [a[0] / 2 - 100, a[1] / 2 + 100], [a[0] / 2 + 100, a[1] / 2 + 100]]

    pygame.draw.polygon(screen, color_dict_for_n_back['green'], position)

    pygame.draw.circle(screen, color_dict_for_n_back["orange"], [a[0] / 2, a[1] / 2], 60)

    pygame.draw.lines(screen, color_dict_for_n_back['white'], False, [[0, 0], [2560, 1440]])
    pygame.draw.lines(screen, color_dict_for_n_back['white'], False, [[2560, 0], [0, 1440]])


#  Обработка событий должна происходить в цикле.
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_pygame()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass

                if event.key == pygame.K_ESCAPE:
                    quit_pygame()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    pass

        pygame.display.update()


pygame_func()
