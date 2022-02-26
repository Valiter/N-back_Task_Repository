

"""Тут находится отслеживание работы клавиш, а также вывод информации на экран с помощью модуля PyGame"""


import pygame
import sys
import time


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


"""Ниже находится функция 'игры' N-Back. Вывод картинки и регистрация нажатий."""
#  Необходимо сделать:
#      1) Вывод картинки.
#      2) Регистрацию нажатий в список и получение этого списка через return.
#      3) Реализовать как-то остслеживание времени? Вопрос.
#      4) Стоит подумать над тем, что именно опрокидывать в функцию.


def pict_and_react():

    """Инициализируем pygame"""

    pygame.init()

    """Ниже будут функции"""

    #  Функция выхода из программы.
    def quit_func():
        pygame.quit()
        sys.exit()

    #  Функция смены картинки.
    def change_stimul():
        print('f')

    """Ниже будут переменные и созданные события"""

    #  Переменные.
    time_in_mill_sec = 1000
    tick_rate = 30
    start_testing = False

    #  Созданные события.
    change_event = pygame.event.Event(pygame.USEREVENT)
    clock = pygame.time.Clock()

    """Ниже находится цикл для обработки событий"""

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quit_func()

            if start_testing is True:
                pygame.time.set_timer(change_event, time_in_mill_sec, True)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_func()

                if event.key == pygame.K_SPACE:
                    if start_testing is False:
                        start_testing = True
                    else:
                        print('s')

            if event.type == pygame.USEREVENT:
                change_stimul()

        clock.tick(tick_rate)



    """Возвращаем информацию"""

    return None


pict_and_react()
