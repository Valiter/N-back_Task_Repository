

"""Тут находится отслеживание работы клавиш, а также вывод информации на экран с помощью модуля PyGame"""


import pygame
import sys
import time


'''Нижу находятся словари-расшифровщики'''


#  Подозреваю, что словарь с фигурами тут не нужен... Или нужно как-то это переработать.
#  Может только позиционирование прописать надо? Непонятно.
figure_dict_for_n_back = {"triangle_up": "", "square": "",
                          "circle": "", "oval": "",
                          "prism": "", "triangle_down": ""}

color_dict_for_n_back = {"white": (255, 255, 255), "red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255),
                         "yellow": (225, 225, 0), "brown": (100, 50, 30), "black": (0, 0, 0), "orange": (255, 100, 25),
                         "beige": (237, 211, 156)}


"""Ниже находится функция 'игры' N-Back. Вывод картинки и регистрация нажатий."""


def pygame_func():

    # list_of_tips = []
    changing_picture = False

    def quit_pygame():
        pygame.quit()
        sys.exit()

    def pict_manager():

        if changing_picture is True:
            print(changing_picture)
            changing_picture is False
            print(changing_picture)

    pygame.init()

    clock = pygame.time.Clock()
    # screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen = pygame.display.set_mode((720, 480))
    window_size = pygame.display.get_window_size()


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

            if pygame.event.get(changing_picture):
                pass


        pict_manager()
        pygame.display.update()


pygame_func()
