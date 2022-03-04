

"""Данный модуль является модулем-экспериментом для создания работающей программы."""


import pygame
import sys
import time
import copy


"""Функция нужно для проверки таймера по событиям."""


def check_func():

    def time_func():
        start = time.monotonic()
        while True:
            result = time.monotonic() - start
            if 2 < result:
                print(start)
                print(result)
                print("Program time: {:>.3f}".format(result) + " seconds.")
                start = time.monotonic()

    pygame.init()
    screen_nums = (720, 480)

    color = {"green": (0, 255, 0), "blue": (0, 0, 255), "red": (255, 0, 0), "white": (255, 255, 255)}
    color_circle = {0: "red", 1: "green", 2: "blue"}
    num_color = 0

    screen = pygame.display.set_mode(screen_nums)

    clock = pygame.time.Clock()

    start_circle = 0
    step = 2
    start = time.monotonic()
    deepcopy_start = copy.deepcopy(start)

    while True:
        start = time.monotonic()

        if start > deepcopy_start + step:
            result = time.monotonic() - deepcopy_start
            deepcopy_start = copy.deepcopy(start)
            print(start)
            print("Program time: {:>.3f}".format(result) + " seconds.")

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.draw.rect(screen, color.get(color_circle.get(num_color)),
                                     (screen_nums[0] / 1 - 50, screen_nums[1] / 1 - 50, 40, 50))
                    num_color += 1
                    if num_color > 2:
                        num_color = 0


        #  Благодаря этим линиям я могу быть уверен в центрировании картинки.
        pygame.draw.line(screen, color.get('blue'), [screen_nums[0], 0], [0, screen_nums[1]])
        pygame.draw.line(screen, color.get('blue'), [screen_nums[0], screen_nums[1]], [0, 0])

        clock.tick(60)
        pygame.display.update()


check_func()
