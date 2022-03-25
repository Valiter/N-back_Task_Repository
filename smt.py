

import pygame
import copy
import time
import sys
import os


def show_stimulus_function(time_to_show_picture, line_of_stimulus, tupe_of_dictionary):
    # С начала получает время к показу, линию стимулов и тип словаря (хотя не очень ясно зачем)
    # Потом нужно сделать вывод с периодикой — но период временной я умею делать через deepcopy
    # А вот вывод картинок... Сделать стимульный ряд из картинок? ПОхоже, что это единственный вариант, ...
    # Чтобы мозги не ебать.

    # Так что... Да.

    pygame.init()

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen.fill((237, 211, 156))
    size = pygame.display.get_window_size()
    length = size[0]
    height = size[1]

    time_1 = time.monotonic()
    time_2 = copy.deepcopy(time_1) + time_to_show_picture

    num = 0

    def quit_func():
        pygame.quit()
        sys.exit()

    def show_picture(name):
        image_show = pygame.image.load(os.path.join("stimuli_img", name + '.png'))
        image_size = pygame.image.load(os.path.join("stimuli_img", name + '.png')).get_size()
        image_size_length = image_size[0]
        image_size_height = image_size[1]
        screen.blit(image_show, ((length / 2) - (image_size_length / 2), (height / 2) - (image_size_height / 2)))

    while True:

        time_1 = time.monotonic()

        if time_1 > time_2 and num < len(line_of_stimulus):
            screen.fill((237, 211, 156))

        if time_1 > time_2 + 0.2:
            time_2 = copy.deepcopy(time_1) + time_to_show_picture

            # И тут мы начинаем что-то делать.
            # Очевидно, что забацаю кучу функций, которые будут легко и просто выносится вне этого цикла, ...
            # Чтобы не мозолить мне глаза.
            if len(line_of_stimulus) > num:
                show_picture(line_of_stimulus[num])
                num += 1
            else:
                print("Программа завершена.")
                show_picture("ura")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_func()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_func()

        pygame.display.update()


show_stimulus_function(2, ['pig', 'fridge', 'teacher'], 1)
