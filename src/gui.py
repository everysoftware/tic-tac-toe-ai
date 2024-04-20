import tkinter as tk
from tkinter import messagebox


class GameGUI:
    def __init__(self, game):
        self.game = game

        self.window = tk.Tk()
        self.window.title("Крестики-нолики")
        self.window.resizable(False, False)

        self.buttons = []
        for i in range(game.rows):
            row = []
            for j in range(game.cols):
                button = tk.Button(
                    self.window,
                    text=" ",
                    width=10,
                    height=5,
                    command=lambda i=i, j=j: self.process_move(i, j),  # noqa
                )
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def process_move(self, row: int, col: int) -> None:
        if self.game.logic.board[row][col] == " ":
            self.game.logic.board[row][col] = self.game.logic.current_player
            self.buttons[row][col]["text"] = self.game.logic.current_player

            if self.game.logic.check_win():
                if messagebox.askyesno(
                    "Победа!",
                    f"Победил игрок {self.game.logic.current_player}! "
                    "Хотите начать новую игру?",
                ):
                    for row in self.buttons:
                        for btn in row:
                            btn: tk.Button
                            btn["text"] = " "
                    self.game.logic.restart()
                else:
                    self.window.quit()
                return

            if self.game.logic.check_draw():
                if messagebox.askyesno(
                    "Ничья!", "Победила дружба!" "Хотите начать новую игру?"
                ):
                    for row in self.buttons:
                        for btn in row:
                            btn: tk.Button
                            btn["text"] = " "
                    self.game.logic.restart()
                else:
                    self.window.quit()
                messagebox.showinfo()
                self.window.quit()
                return

            self.game.logic.current_player = (
                self.game.o_label
                if self.game.logic.current_player == self.game.x_label
                else self.game.x_label
            )

            self.game.logic.make_move()
