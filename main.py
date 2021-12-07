
#TODO Detect if one of the users won by some kind of msg or something

import pygame, sys, random
from pygame.locals import *

pygame.init()

# Colours
BACKGROUND = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
LINE_WIDTH = 15
# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
SQUARE_SIZE = 200
BOARD_ROWS = 3
BOARD_COLS = 3

CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15

CROSS_WIDTH = 25
CROSS_COLOR = (255, 255, 255)
SPACE = 55
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Tic Tac Toe')


def draw_lines():
    """Draws grid 3x3 by lines"""
    # 1 horizontal
    pygame.draw.line(WINDOW, LINE_COLOR, (0, 200), (WINDOW_WIDTH, 200), LINE_WIDTH)
    # 2 horizontal
    pygame.draw.line(WINDOW, LINE_COLOR, (0, 400), (WINDOW_WIDTH, 400), LINE_WIDTH)
    # 1 vertical
    pygame.draw.line(WINDOW, LINE_COLOR, (200, 0), (200, WINDOW_HEIGHT), LINE_WIDTH)
    # 2 vertical
    pygame.draw.line(WINDOW, LINE_COLOR, (400, 0), (400, WINDOW_HEIGHT), LINE_WIDTH)


def get_segment(mouse_pos) -> (int, int):
    """returns cords clicked square"""
    mouse_x = mouse_pos[0] // 200
    mouse_y = mouse_pos[1] // 200
    return (mouse_y, mouse_x)  # coords are reverted because of the screen


def is_board_full(game_board) -> bool:
    """returns false if board have empty space"""
    for i in range(len(game_board)):
        for j in range(len(game_board)):
            if game_board[i][j] == 0:
                return False
            else:
                return True


def available_square(game_board, row, col):
    return game_board[row][col] == 0


def place_latter(game_board, row, col, latter):
    """places latter at specific square of the game_board"""
    game_board[row][col] = latter
    return game_board


def draw_figures(game_board):
    for row in range(len(game_board)):
        for col in range(len(game_board)):
            if game_board[row][col] == 1: #draw circle
                pygame.draw.circle(WINDOW, LINE_COLOR, (int(col * 200 + 100), int(row * 200 + 100)), CIRCLE_RADIUS,
                                   CIRCLE_WIDTH)
            elif game_board[row][col] == 2: #draw crosses
                pygame.draw.line(WINDOW, CROSS_COLOR,
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(WINDOW, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 CROSS_WIDTH)


# The main function that controls the game
def main():
    game_board = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
    print(is_board_full(game_board))
    looping = True
    player = 1
    # The main game loop
    while looping:
        # Get inputs
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_click_pos = pygame.mouse.get_pos()
                # calc segment
                clicked_row, clicked_col = get_segment(mouse_click_pos)
                if available_square(game_board, clicked_row, clicked_col):
                    if player == 1:
                        game_board = place_latter(game_board, clicked_row, clicked_col, 1)

                        player = 2
                    elif player == 2:
                        game_board = place_latter(game_board, clicked_row, clicked_col, 2)
                        player = 1

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Processing
        # print(mouse_click_pos)

        # Render elements of the game
        WINDOW.fill(BACKGROUND)
        draw_lines()
        draw_figures(game_board)  # TODO probably move it to player zone
        pygame.display.update()
        fpsClock.tick(FPS)


main()
