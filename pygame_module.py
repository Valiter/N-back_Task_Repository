

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

picture_dictionary = ["again", "good", "ura", "enter", "pause", "ball", "ball_face", "ball_on_tree",
                      "boy_musition", "bucket", "cat", "computer", "cop", "doctor", "duck",
                      "elza", "family", "fire_quard", "flower_2", "flower", "fridge", "frog",
                      "girl_painter", "good", "grandmother", "jam", "jerry", "lion", "man", "mouse",
                      "blank", "phone", "pig", "popcorn", "pot", "reader", "snake", "sun",
                      "teacher", "tree", "turtle", "warrior", "watermelon", "driver", "red_car",
                      "builder"]

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
    tick_rate = 60
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

    """Ниже будут функции"""

    #  Функция выхода из программы.
    def quit_func():
        pygame.quit()
        sys.exit()

    #  Функция смены картинки.
    def change_stimulus():
        pygame.draw.circle(screen, color_dict_for_n_back['white'],
                           [(length / 2), (height / 2)], 150)

    def picture_changer():
        pass

    """Ниже находится цикл для обработки событий"""

    while True:

        start_time = time.monotonic()

        if start_time > end_time + time_to_show:
            end_time = copy.deepcopy(start_time)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.QUIT or pygame.K_ESCAPE:
                    quit_func()

        pygame.display.update()
        clock.tick(tick_rate)


pict_and_react(1)
