

"""Тут находится отслеживание работы клавиш, а также вывод информации на экран с помощью модуля PyGame"""


import pygame
import sys
import time
import copy

'''Нижу находятся словари-расшифровщики'''


#  Подозреваю, что словарь с фигурами тут не нужен... Или нужно как-то это переработать.
#  Может только позиционирование прописать надо? Непонятно.
#  Вообще, можно вызывать функции!!! Это клево. Например, можно вызывать необходимую хрень, ...
#  Которая будет делать что мне надо.
figure_dict_for_n_back = {"triangle_up": "", "square": "",
                          "circle": "", "oval": "",
                          "prism": "", "triangle_down": ""}

color_dict_for_n_back = {"white": (255, 255, 255), "red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255),
                         "yellow": (225, 225, 0), "brown": (100, 50, 30), "black": (0, 0, 0), "orange": (255, 100, 25),
                         "beige": (237, 211, 156)}

dict_for_choose_color = {0: "white", 1: "red", 2: "green", 3: "blue", 4: "yellow",
                         5: "brown", 6: "black", 7: "orange", 8: "beige"}


"""Ниже находится функция 'игры' N-Back. Вывод картинки и регистрация нажатий."""
#  Необходимо сделать:
#      1) Вывод картинки.
#      2) Регистрацию нажатий в список и получение этого списка через return.
#      3) Реализовать как-то остслеживание времени? Вопрос.
#      4) Стоит подумать над тем, что именно опрокидывать в функцию.


def pict_and_react(time_for_showing):

    """Инициализируем pygame"""

    pygame.init()

    """Ниже будут переменные и созданные события"""

    #  Объявляем размер окна.
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    #  Переменные.
    screen_info = pygame.display.get_window_size()
    length = screen_info[0]
    height = screen_info[1]

    # Тут логические переменные и переменные для скорости отрисовки.
    tick_rate = 30
    start_testing = False

    # Тут переменные связанные с временем.
    start_time = time.monotonic()
    end_time = copy.deepcopy(start_time)
    time_to_show = 1
    time_in_mill_sec = time_for_showing * 500

    # Тут переменные связанные с цветом
    color = 0

    #  Созданные события.
    clock = pygame.time.Clock()

    # Переменные связанные с позиционированием.
    circle_x = 0
    circle_y = 0
    circle_move_x = None
    circle_move_y = None
    position = [(length / 3) + circle_x, (height / 4) + circle_y]

    """Ниже будут функции"""

    #  Функция выхода из программы.
    def quit_func():
        pygame.quit()
        sys.exit()

    #  Функция смены картинки.
    def change_stimulus(position_in_func, sec_position_in_func):
        pygame.draw.circle(screen, color_dict_for_n_back['black'],
                           sec_position_in_func, 50)
        pygame.draw.circle(screen, color_dict_for_n_back['white'],
                           position_in_func, 50)

    """Ниже находится цикл для обработки событий"""

    while True:

        start_time = time.monotonic()

        if start_time > end_time + time_to_show:
            end_time = copy.deepcopy(start_time)
            pygame.draw.circle(screen, color_dict_for_n_back[dict_for_choose_color[color]],
                               [(length / 2), (height / 2)], 60)
            color += 1
            if color == 8:
                color = 0

        if circle_move_x is True:
            circle_x -= 10
        if circle_move_x is False:
            circle_x += 10
        if circle_move_y is True:
            circle_y -= 10
        if circle_move_y is False:
            circle_y += 10

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quit_func()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_func()

                if event.key == pygame.K_DOWN:
                    circle_move_y = False
                if event.key == pygame.K_UP:
                    circle_move_y = True
                if event.key == pygame.K_LEFT:
                    circle_move_x = True
                if event.key == pygame.K_RIGHT:
                    circle_move_x = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    circle_move_y = None
                if event.key == pygame.K_UP:
                    circle_move_y = None
                if event.key == pygame.K_LEFT:
                    circle_move_x = None
                if event.key == pygame.K_RIGHT:
                    circle_move_x = None

        sec_position = copy.deepcopy(position)
        position = [(length / 3) + circle_x, (height / 4) + circle_y]
        change_stimulus(position, sec_position)

        pygame.display.update()
        clock.tick(tick_rate)


pict_and_react(1)
