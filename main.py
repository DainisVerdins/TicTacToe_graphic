import pygame, sys, random
from pygame.locals import *

pygame.init()

# Colours
BACKGROUND = (28, 170, 156)
LINE_COLOR = (23, 145, 135)

# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Tic Tac Toe')


def draw_lines():
    """Draws grid 3x3 by lines"""
    # 1 horizontal
    pygame.draw.line(WINDOW, LINE_COLOR, (0, 200), (WINDOW_WIDTH, 200), 10)
    # 2 horizontal
    pygame.draw.line(WINDOW, LINE_COLOR, (0, 400), (WINDOW_WIDTH, 400), 10)
    # 1 vertical
    pygame.draw.line(WINDOW, LINE_COLOR, (200, 0), (200, WINDOW_HEIGHT), 10)
    # 2 vertical
    pygame.draw.line(WINDOW, LINE_COLOR, (400, 0), (400, WINDOW_HEIGHT), 10)



# The main function that controls the game
def main():
    looping = True

    # The main game loop
    while looping:
        # Get inputs
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Processing
        # This section will be built out later

        # Render elements of the game
        WINDOW.fill(BACKGROUND)
        draw_lines()
        pygame.display.update()
        fpsClock.tick(FPS)


main()
