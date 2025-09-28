import pygame

import config
from logic.board import Board
from drawing.draw import draw_board

pygame.init()
screen = pygame.display.set_mode(config.WINDOW_SIZE)
running = True

board = Board(config.BOARD_SIZE[0], config.BOARD_SIZE[1], config.N_MINES)
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
                board = Board(config.BOARD_SIZE[0], config.BOARD_SIZE[1], config.N_MINES)
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
            if not board.mines_placed:
                board.reset_board(x, y)  
            if event.button == 1:
                board.handle_reveal(x, y)
            elif event.button == 3:
                board.place_flag(x, y)                    

pygame.quit()
