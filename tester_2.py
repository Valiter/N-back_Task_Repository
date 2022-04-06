

import pygame
import copy
import time
import sys
import os


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

ru_letter_list_bl = ["А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л",
                     "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш",
                     "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"]

eng_letter_list_bl = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                      "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
                      "Y", "Z"]

numbers_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def show_stimulus_function(time_to_show_picture, line_of_stimulus):
    # С начала получает время к показу, линию стимулов и тип словаря (хотя не очень ясно зачем)
    # Потом нужно сделать вывод с периодикой — но период временной я умею делать через deepcopy
    # А вот вывод картинок... Сделать стимульный ряд из картинок? ПОхоже, что это единственный вариант, ...
    # Чтобы мозги не ебать.

    pygame.init()

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    size = pygame.display.get_window_size()
    length = size[0]
    height = size[1]

    time_1 = time.monotonic()
    time_2 = copy.deepcopy(time_1) + time_to_show_picture
    clock = pygame.time.Clock()

    num = 0
    reaction = None
    list_of_reactions = []

    def fill_and_print_pictures():
        if line_of_stimulus[0] in picture_list:
            fon_fill = color_dict_for_n_back['beige']
        else:
            fon_fill = color_dict_for_n_back['white']

        return fon_fill

    def quit_func():
        pygame.quit()
        sys.exit()

    def show_picture(name, color):
        image_show = pygame.image.load(os.path.join("stimuli_img", name + '.png'))
        image_show = pygame.transform.scale(image_show, [1024, 720])
        image_size = image_show.get_size()
        image_size_length = image_size[0]
        image_size_height = image_size[1]
        first_point = (length / 2) - (image_size_length / 2)
        second_point = (height / 2) - (image_size_height / 2)
        screen.blit(image_show, (first_point, second_point))

        pygame.draw.rect(screen, color_dict_for_n_back['red'], [first_point + image_size_length - 10,
                                         second_point - 10, 50, image_size_height + 30])
        pygame.draw.rect(screen, color_dict_for_n_back['yellow'], [first_point - 10, second_point - 10, 50,
                                         image_size_height + 20])
        pygame.draw.rect(screen, color_dict_for_n_back['green'], [first_point - 10,
                                         second_point + image_size_height - 10,
                                         image_size_length + 20, 30])
        pygame.draw.rect(screen, color_dict_for_n_back['blue'], [first_point - 10, second_point - 10,
                                         image_size_length + 20, 30])

    def line_of_remaining_time(time_step, time_mono_tick_1, time_mono_tick_2, color):
        time_line = time_mono_tick_2 - time_mono_tick_1
        pygame.draw.rect(screen, color_dict_for_n_back['black'], [length / 4, 5,
                         (2 * (length / 4)), 15])
        pygame.draw.rect(screen, color, [length / 4, 5,
                         (2 * (length / 4)) / time_step * time_line, 15])

    color_of_fon = fill_and_print_pictures()
    screen.fill(color_of_fon)

    while True:
        time_1 = time.monotonic()

        if time_1 > time_2 and num < len(line_of_stimulus):
            screen.fill(color_of_fon)

        if time_1 > time_2 + 1:
            time_2 = copy.deepcopy(time_1) + time_to_show_picture

            list_of_reactions.append(reaction)
            reaction = False
            # И тут мы начинаем что-то делать.
            # Очевидно, что забацаю кучу функций, которые будут легко и просто выносится вне этого цикла, ...
            # Чтобы не мозолить мне глаза.
            if len(line_of_stimulus) > num:
                show_picture(line_of_stimulus[num], color_of_fon)
                num += 1
            else:
                print("Программа завершена.")
                screen.fill(color_of_fon)
                return list_of_reactions

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_func()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_func()
                if event.key == pygame.K_SPACE:
                    reaction = True

        line_of_remaining_time(time_to_show_picture, time_1, time_2, color_of_fon)
        clock.tick(120)
        pygame.display.update()


list_a = ['A', 'B', 'A', 'B']
a = show_stimulus_function(3, list_a)
print(a)

# un_stimulus, end_line, true_false_results, time_to_show = tester_1.main_function()
# show_stimulus_function(str(time_to_show), end_line)
