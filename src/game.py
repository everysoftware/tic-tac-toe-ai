from src.gui import GameGUI


class Game:
    x_label = "X"
    o_label = "O"

    def __init__(self, mechanic, rows, cols, win_length):
        self.rows = rows
        self.cols = cols
        self.win_length = win_length

        # Стратегия
        self.logic = mechanic(self)
        self.gui = GameGUI(self)

    def run(self) -> None:
        self.gui.window.mainloop()
