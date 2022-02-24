import pygame
import sys
from random import randint

size = width, height = 800, 600
black = 0, 0, 0
colors = [(0, 255, 0), (0, 0, 255), (255, 0, 0)]


def main():
    pygame.init()

    screen = pygame.display.set_mode(size)
    color = colors[0]
    counter = 0
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        screen.fill(black)
        pygame.draw.circle(screen, color, (width // 2, height // 2), 250)
        counter += 1
        if counter > 10:
            color = colors[randint(0, 2)]
            counter = 0

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == '__main__':
    main()
    pygame.quit()