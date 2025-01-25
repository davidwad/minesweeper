from random import sample

from logic.square import Square
from utils.grid import get_neighbours


class Board:
    def __init__(self, width: int, height: int, n_mines: int):
        self.height = height
        self.width = width
        self.n_mines = n_mines

        self._initialize_board()
        self._place_mines()
        self._calculate_danger(1)
        self._calculate_danger(2)

    def get_squares(self) -> list[Square]:
        return sum(self.board, [])

    def get_square(self, x: int, y: int) -> Square:
        return self.board[x][y]

    def handle_reveal(self, x: int, y: int):
        if x < 0 or x >= self.width:
            return
        if y < 0 or y >= self.height:
            return
        square = self.get_square(x, y)
        if square.revealed:
            return
        if square.mine:
            # TODO: Reveal all mines
            square.reveal()
            return
        self._reveal_safe_squares(x, y)

    def place_flag(self, x: int, y: int):
        if x < 0 or x >= self.width:
            return
        if y < 0 or y >= self.height:
            return
        self.get_square(x, y).toggle_flag()

    def _initialize_board(self):
        self.board: list[list[Square]] = []
        for x in range(self.width):
            col = []
            for y in range(self.height):
                col.append(Square(x, y))
            self.board.append(col)

    def _place_mines(self):
        for square in sample(self.get_squares(), self.n_mines):
            square.mine = True

    def _calculate_danger(self, distance: int):
        for s in self.get_squares():
            n_adjacent_mines = 0
            for x, y in get_neighbours(s.x, s.y, distance, self.width, self.height):
                if self.get_square(x, y).mine:
                    n_adjacent_mines += 1
            s.danger[distance] = n_adjacent_mines

    def _reveal_safe_squares(self, x: int, y: int):
        square = self.get_square(x, y)
        square.reveal()
        if square.danger[1] == 0:
            for xx, yy in get_neighbours(x, y, 1, self.width, self.height):
                if not self.get_square(xx, yy).revealed:
                    self._reveal_safe_squares(xx, yy)
