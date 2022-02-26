

"""Данный модуль является модулем-экспериментом для создания работающей программы."""


import pygame
import sys


"""Функция нужно для проверки таймера по событиям."""


def check_func():

    pygame.init()
    screen_nums = (720, 480)

    color = {"green": (0, 255, 0), "blue": (0, 0, 255), "red": (255, 0, 0), "white": (255, 255, 255)}
    color_circle = {0: "red", 1: "green", 2: "blue"}
    screen = pygame.display.set_mode(screen_nums)

    clock = pygame.time.Clock()

    start_circle = 0
    pict_changer = pygame.event.Event(pygame.USEREVENT)

    print(pict_changer)
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if True:
                pygame.time.set_timer(pict_changer, 1000)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.Surface.fill(screen, color.get('white'))

            if event.type == pygame.USEREVENT:
                if event == pict_changer:
                    pygame.draw.rect(screen, color.get(color_circle.get(start_circle)),
                                     (screen_nums[0] / 2 - 50, screen_nums[1] / 2 - 50, 100, 100))
                    start_circle += 1
                    if start_circle > 2:
                        start_circle = 0

        #  Благодаря этим линиям я могу быть уверен в центрировании картинки.
        pygame.draw.line(screen, color.get('blue'), [screen_nums[0], 0], [0, screen_nums[1]])
        pygame.draw.line(screen, color.get('blue'), [screen_nums[0], screen_nums[1]], [0, 0])

        clock.tick(120)

        pygame.display.update()


check_func()
