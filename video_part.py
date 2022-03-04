

"""Данный модуль является модулем-экспериментом для создания работающей программы."""


import pygame
import sys
import time


"""Функция нужно для проверки таймера по событиям."""


def check_func():

    pygame.init()
    screen_nums = (720, 480)

    color = {"green": (0, 255, 0), "blue": (0, 0, 255), "red": (255, 0, 0), "white": (255, 255, 255)}
    color_circle = {0: "red", 1: "green", 2: "blue"}
    num_color = 0

    screen = pygame.display.set_mode(screen_nums)

    clock = pygame.time.Clock()

    start_circle = 0
    pict_changer = pygame.event.Event(pygame.USEREVENT)

    n = 1
    alpha_time = 0
    beta_time = alpha_time + n
    print(pict_changer)

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.draw.rect(screen, color.get('green'),
                                     (screen_nums[0] / 1 - 50, screen_nums[1] / 1 - 50, 40, 50))
                if event.key == pygame.K_SPACE:
                    if start_circle == 0:
                        start_circle = 1

            if start_circle == 1:
                if alpha_time == 0:
                    alpha_time = time.time()
                elif alpha_time <= beta_time:
                    pass
                else:
                    alpha_time = time.time()

                if beta_time == alpha_time:
                    pygame.draw.rect(screen, color.get(color_circle[num_color]),
                                     (screen_nums[0] / 2 - 50, screen_nums[1] / 2 - 50, 100, 100))
                    num_color += 1
                    if num_color > 2:
                        num_color = 0

        #  Благодаря этим линиям я могу быть уверен в центрировании картинки.
        pygame.draw.line(screen, color.get('blue'), [screen_nums[0], 0], [0, screen_nums[1]])
        pygame.draw.line(screen, color.get('blue'), [screen_nums[0], screen_nums[1]], [0, 0])

        clock.tick(60)

        pygame.display.update()


check_func()
