

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


def pict_and_react(time_for_showing, gived_line_of_stimulus, type_of_stimulus, name, date):

    """Инициализируем pygame"""

    pygame.init()

    """Ниже будут переменные и созданные события"""

    #  Объявляем размер окна.
    screen_info = pygame.display.get_desktop_sizes()
    length = screen_info[0][0]
    height = screen_info[0][1]

    screen = pygame.display.set_mode((length, height))
    # screen = pygame.display.set_mode((2560, 1920))
    screen.fill(color_dict_for_n_back["black"])

    #  Переменные связанные с размерами окна.
    # screen_info = pygame.display.get_window_size()
    # length = screen_info[0]
    # height = screen_info[1]

    # Список, необходимый для запоминания нажатий.
    take_reaction = []
    index_num = 0
    length_of_line_of_stimulus = len(gived_line_of_stimulus)
    reaction_added = False

    #  Созданные события.
    clock = pygame.time.Clock()

    """Проверка для использования списка с картинками для вывода стимулов."""

    # Переменная для определения типа списка с картинками.
    type_of_pictures_and_stimulus = None
    color = None

    # Это очень корявый способ работы для программы.
    # Русские буквы.
    if type_of_stimulus == 1:
        type_of_pictures_and_stimulus = ru_letter_list
        color = color_dict_for_n_back['white']
    # Английские буквы.
    elif type_of_stimulus == 2:
        type_of_pictures_and_stimulus = eng_letter_list
        color = color_dict_for_n_back['white']
    # Числа.
    elif type_of_stimulus == 3:
        type_of_pictures_and_stimulus = numbers_list
        color = color_dict_for_n_back['white']
    # Фигуры.
    elif type_of_stimulus == 4:
        type_of_pictures_and_stimulus = figure_dict_for_n_back
        color = color_dict_for_n_back['white']
    # Цвета.
    elif type_of_stimulus == 5:
        type_of_pictures_and_stimulus = color_dict_for_n_back
        color = color_dict_for_n_back['white']
    # Картинки.
    elif type_of_stimulus == 6:
        type_of_pictures_and_stimulus = picture_list
        color = color_dict_for_n_back['beige']

    # Тут мы создаем ПУСТОЙ список с необходимой нам длиной.
    while len(take_reaction) < length_of_line_of_stimulus:
        take_reaction.append(False)

    """Ниже находятся функции"""

    #  Функция выхода из программы.
    def quit_func(reaction):
        print(reaction)
        pygame.quit()
        sys.exit()

    def writing(name_student, date_student, take_reaction_i):
        log_file = name_student + '_' + date_student + '.txt'
        results = open('.//results//' + log_file, 'a')
        results.writelines(str(take_reaction_i))
        results.write('\n')
        results.close()

    def get_pressed(index, line, reaction_type):
        reaction_type = True
        index -= 1
        print(index)
        line.insert(index, True)
        return reaction_type, line

    def change_stimulus(name, color_in):
        image_show = pygame.image.load(os.path.join("stimuli_img", str(name) + '.png'))
        image_show = pygame.transform.scale(image_show, [1024, 720])
        image_size = image_show.get_size()
        image_size_length = image_size[0]
        image_size_height = image_size[1]

        first_point = (length / 2) - (image_size_length / 2)
        second_point = (height / 2) - (image_size_height / 2)

        screen.blit(image_show, (first_point, second_point))

        pygame.draw.rect(screen, color_in, [first_point + image_size_length - 10,
                         second_point - 10, 50, image_size_height + 30])
        pygame.draw.rect(screen, color_in, [first_point - 10, second_point - 10, 50,
                         image_size_height + 20])
        pygame.draw.rect(screen, color_in, [first_point - 10,
                         second_point + image_size_height - 10,
                         image_size_length + 20, 30])
        pygame.draw.rect(screen, color_in, [first_point - 10, second_point - 10,
                         image_size_length + 20, 30])

    """НЕ РАБОТАЕТ ПОЛОСКА ВРЕМЕНИ!!!!"""
    def line_of_remaining_time(time_step, time_mono_tick_1, time_mono_tick_2, color_in):
        time_line = time_mono_tick_2 - time_mono_tick_1
        pygame.draw.rect(screen, color_dict_for_n_back['black'], [length / 4, 5,
                         (2 * (length / 4)), 15])
        pygame.draw.rect(screen, color_in, [length / 4, 5, (2 * (length / 4)) / time_step * time_line, 15])
    """Ниже находится цикл для обработки событий"""

    # Тут переменные связанные с временем.
    start_time = time.monotonic()
    end_time = copy.deepcopy(start_time) + time_for_showing

    while True:

        start_time = time.monotonic()
        if start_time > end_time:
            screen.fill(color)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                writing(name, date, take_reaction)
                quit_func(take_reaction)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    writing(name, date, take_reaction)
                    quit_func(take_reaction)
                if event.key == pygame.K_SPACE:
                    print("pr")
                    if reaction_added is False:
                        print(index_num)
                        reaction_added, take_reaction = get_pressed(index_num, take_reaction, reaction_added)
                        print(index_num, 'key')
                    print(take_reaction)

        # В проверке ниже будет происходит замена картинок по истечению времени.
        if start_time > end_time + 0.1:
            end_time = copy.deepcopy(start_time) + time_for_showing
            if length_of_line_of_stimulus > index_num:
                change_stimulus(gived_line_of_stimulus[index_num], color)
                index_num += 1
                print(index_num, 'pict')
                reaction_added = False
            else:
                print('Program is finished.')
                writing(name, date, take_reaction)
                quit_func(take_reaction)

        line_of_remaining_time(time_for_showing, start_time, end_time + 0.1, color)
        pygame.display.update()

    # # ЗАПУСТИТЬ tkinter
    # main_file_circle.main_func()
