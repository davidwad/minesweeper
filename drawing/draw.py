import pygame

import config
from logic.square import Square
from logic.board import Board

pygame.font.init()
font = pygame.font.SysFont(None, int(config.SCALE * 1.5))


def draw_board(screen: pygame.Surface, board: Board, distance: int):
    for s in board.get_squares():
        draw_square(screen, s, distance)


def draw_square(screen: pygame.Surface, square: Square, distance: int):
    rect = pygame.rect.Rect(
        square.x * config.SCALE + config.GAP,
        square.y * config.SCALE + config.GAP,
        config.SCALE - config.GAP,
        config.SCALE - config.GAP
    )
    if square.revealed:
        if square.mine:
            pygame.draw.rect(screen, "black", rect)
        else:
            danger = square.danger[distance]
            pygame.draw.rect(screen, "white", rect)
            if danger > 0:
                img = font.render(str(danger), True, "black")
                screen.blit(img, rect)
    else:
        pygame.draw.rect(screen, "grey", rect)
        if square.flag:
            pygame.draw.circle(screen, "red", rect.center, (rect.width / 3))
