import pygame
import sys


"""Функция нужно для проверки таймера по событиям."""


def check_func():

    pygame.init()
    screen_nums = (720, 480)

    color = {"green": (0, 255, 0), "blue": (0, 0, 255), "red": (255, 0, 0)}
    color_circle = {0: "red", 1: "green", 2: "blue"}
    screen = pygame.display.set_mode(screen_nums)

    clock = pygame.time.Clock()

    start_circle = 0
    pict_changer = pygame.event.Event(pygame.USEREVENT)

    pygame.draw.rect(screen, color.get('green'), (screen_nums[0] / 2 - 50, screen_nums[1] / 2 - 50, 100, 100))
    print(pict_changer)
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass

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

        pygame.time.set_timer(pict_changer, 3000, False)

        clock.tick(30)

        pygame.display.update()


check_func()
