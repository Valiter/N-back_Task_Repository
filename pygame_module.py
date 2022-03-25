

"""Тут находится отслеживание работы клавиш, а также вывод информации на экран с помощью модуля PyGame"""


import pygame
import sys
import time
import copy
import os


'''Нижу находятся словари-расшифровщики'''


#  Подозреваю, что словарь с фигурами тут не нужен... Или нужно как-то это переработать.
#  Может только позиционирование прописать надо? Непонятно.
#  Вообще, можно вызывать функции!!! Это клево. Например, можно вызывать необходимую хрень, ...
#  Которая будет делать что мне надо.
figure_dict_for_n_back = {"triangle_up": "triangle_up", "square": "square",
                          "circle": "circle", "oval": "oval",
                          "prism": "prism", "triangle_down": "triangle_down"}

color_dict_for_n_back = {"white": (255, 255, 255), "red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255),
                         "yellow": (225, 225, 0), "brown": (100, 50, 30), "black": (0, 0, 0), "orange": (255, 100, 25),
                         "beige": (237, 211, 156)}

dict_for_choose_color = {0: "white", 1: "red", 2: "green", 3: "blue", 4: "yellow",
                         5: "brown", 6: "black", 7: "orange", 8: "beige"}

picture_list = ["again", "good", "ura", "enter", "pause", "ball", "ball_face", "ball_on_tree",
                "boy_musition", "bucket", "cat", "computer", "cop", "doctor", "duck",
                "elza", "family", "fire_quard", "flower_2", "flower", "fridge", "frog",
                "girl_painter", "good", "grandmother", "jam", "jerry", "lion", "man", "mouse",
                "blank", "phone", "pig", "popcorn", "pot", "reader", "snake", "sun",
                "teacher", "tree", "turtle", "warrior", "watermelon", "driver", "red_car",
                "builder"]

ru_letter_list = ["a", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л",
                  "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш",
                  "щ", "ъ", "ы", "ь", "э", "ю", "я"]

eng_letter_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                   "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                   "y", "z"]

numbers_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


"""Ниже находится функция 'игры' N-Back. Вывод картинки и регистрация нажатий."""
#  Необходимо сделать:
#      1) Вывод картинки.
#      2) Регистрацию нажатий в список и получение этого списка через return.
#      3) Реализовать как-то остслеживание времени? Вопрос.
#      4) Стоит подумать над тем, что именно опрокидывать в функцию.


def pict_and_react(time_for_showing, gived_line_of_stimulus, type_of_stimulus):

    """Инициализируем pygame"""

    pygame.init()

    """Ниже будут переменные и созданные события"""

    #  Объявляем размер окна.
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen.fill(color_dict_for_n_back["beige"])

    #  Переменные связанные с размерами окна.
    screen_info = pygame.display.get_window_size()
    length = screen_info[0]
    height = screen_info[1]

    # Список, необходимый для запоминания нажатий.
    take_reaction = []
    index_num = 0
    length_of_line_of_stimulus = len(gived_line_of_stimulus)

    # Тут переменные связанные с временем.
    start_time = time.monotonic()
    end_time = copy.deepcopy(start_time)

    #  Созданные события.
    clock = pygame.time.Clock()

    """Проверка для использования списка с картинками для вывода стимулов."""

    # Переменная для определения типа списка с картинками.
    type_of_pictures_and_stimulus = None
    color = None

    # Русские буквы.
    if type_of_stimulus == 1:
        type_of_pictures_and_stimulus = ru_letter_list
        color = None
    # Английские буквы.
    elif type_of_stimulus == 2:
        type_of_pictures_and_stimulus = eng_letter_list
        color = None
    # Числа.
    elif type_of_stimulus == 3:
        type_of_pictures_and_stimulus = numbers_list
        color = None
    # Фигуры.
    elif type_of_stimulus == 4:
        type_of_pictures_and_stimulus = figure_dict_for_n_back
        color = None
    # Цвета.
    elif type_of_stimulus == 5:
        type_of_pictures_and_stimulus = color_dict_for_n_back
        color = None
    # Картинки.
    elif type_of_stimulus == 6:
        type_of_pictures_and_stimulus = picture_list
        color = ("beige")

    """Ниже находятся функции"""

    #  Функция выхода из программы.
    def quit_func():
        pygame.quit()
        sys.exit()

    def check_type(needed_to_check):
        if type(needed_to_check) is dict:
            return 2
        if type(needed_to_check) is list:
            return 1

    def get_pressed():
        pass

    def change_stimulus(name, color_3):
        color_2 = color_dict_for_n_back(color_3)
        image = pygame.image.load(os.path.join("stimuli_img", name + '.png'))
        screen.blit(image, ((length / 2) - 683, (height / 2) - 384))
        pygame.draw.rect(screen, color_dict_for_n_back[color_2],
                         [length / 2 - 700, height / 2 - 400, length / 2 + 150, height / 2 - 690])
        pygame.draw.rect(screen, color_dict_for_n_back[color_2],
                         [length / 2 - 700, height / 2 + 380, length / 2 + 150, height / 2 - 690])
        pygame.draw.rect(screen, color_dict_for_n_back[color_2],
                         [length / 2 - 700, height / 2 - 400, 30, 800])
        pygame.draw.rect(screen, color_dict_for_n_back[color_2],
                         [length / 2 + 680, height / 2 - 400, 30, 800])

    """Ниже находится цикл для обработки событий"""

    while True:

        start_time = time.monotonic()

        if start_time > end_time + time_for_showing:
            screen.fill(color_dict_for_n_back['beige'])

        # В проверке ниже будет происходит замена картинок по истечению времени.
        if start_time > end_time + time_for_showing + 0.1:
            if length_of_line_of_stimulus > index_num:
                end_time = copy.deepcopy(start_time)

                change_stimulus(gived_line_of_stimulus[index_num], color)

                index_num += 1
            else:
                print('Program is finished.')
                quit_func()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_func()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_func()
                if event.key == pygame.K_SPACE:
                    get_pressed()

        pygame.display.update()


list_a = ['pig', 'fridge', 'teacher',
          'teacher', 'pig', 'fridge',
          'fridge', 'fridge', 'sun',
          'sun', 'fridge', 'pig', 'pig',
          'fridge', 'fridge', 'fire_quard',
          'teacher', 'fire_quard', 'teacher', 'sun']

pict_and_react(1, list_a, 6)
