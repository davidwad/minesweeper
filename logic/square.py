

class Square:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.mine = None
        self.flag = False
        self.revealed = False
        self.danger = {}

    def reveal(self):
        self.revealed = True

    def toggle_flag(self):
        self.flag = not self.flag
