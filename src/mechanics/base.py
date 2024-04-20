import abc


class MechanicBase(abc.ABC):
    def __init__(self, game):
        self.game = game
        self.board = [[" "] * game.cols for _ in range(game.rows)]
        self.current_player = self.game.x_label

    def restart(self):
        self.board = [[" "] * self.game.cols for _ in range(self.game.rows)]
        self.current_player = self.game.x_label

    def check_win(self):
        height, width = self.game.rows, self.game.cols
        win_length = self.game.win_length
        board = self.board

        for i in range(height):
            for j in range(width):
                if board[i][j] == " ":
                    continue
                if j + win_length <= width and all(
                    board[i][j + k] == board[i][j] for k in range(win_length)
                ):
                    return True
                if i + win_length <= height and all(
                    board[i + k][j] == board[i][j] for k in range(win_length)
                ):
                    return True
                if (
                    j + win_length <= width
                    and i + win_length <= height
                    and all(
                        board[i + k][j + k] == board[i][j] for k in range(win_length)
                    )
                ):
                    return True
                if (
                    j - win_length >= -1
                    and i + win_length <= height
                    and all(
                        board[i + k][j - k] == board[i][j] for k in range(win_length)
                    )
                ):
                    return True
        return False

    def check_draw(self) -> bool:
        return all(cell != " " for row in self.board for cell in row)

    # "Шаблонный метод"
    @abc.abstractmethod
    def make_move(self) -> None: ...
