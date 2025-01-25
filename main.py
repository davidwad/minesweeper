import pygame

import config
from logic.board import Board
from drawing.draw import draw_board

pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True

board = Board(30, 20, 100)
distance = 1

while running:
    draw_board(screen, board, distance)
    pygame.display.flip()

    event = pygame.event.wait()
    match event.type:
        case pygame.QUIT:
            running = False
        case pygame.KEYUP:
            if event.key == pygame.K_r:
                board = Board(30, 20, 100)
                distance = 1
        case pygame.MOUSEWHEEL:
            if distance == 1:
                distance = 2
            else:
                distance = 1
        case pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            x = int(x / config.SCALE)
            y = int(y / config.SCALE)
            if event.button == 1:
                board.handle_reveal(x, y)
            elif event.button == 3:
                board.place_flag(x, y)

pygame.quit()
