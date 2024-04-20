from src.mechanics.base import MechanicBase


class AIMechanic(MechanicBase):
    def __init__(self, game):
        super().__init__(game)

    def make_move(self) -> None:
        if self.game.logic.current_player == self.game.x_label:
            return

        best_score = float("-inf")
        move = None
        alpha = float("-inf")
        beta = float("inf")

        for i in range(self.game.rows):
            for j in range(self.game.cols):
                if self.board[i][j] == " ":
                    self.board[i][j] = self.game.logic.current_player
                    score = self._minimax(alpha, beta)
                    self.board[i][j] = " "

                    if score > best_score:
                        best_score = score
                        move = (i, j)

        self.game.gui.process_move(*move)

    def _minimax(
        self, alpha: float, beta: float, depth: int = 0, is_maximizing: bool = False
    ) -> int:
        if self.check_win():
            return 1 if self.game.logic.current_player == self.game.o_label else -1
        elif self.check_draw():
            return 0

        if is_maximizing:
            best_score = float("-inf")

            for i in range(self.game.rows):
                for j in range(self.game.cols):
                    if self.board[i][j] == " ":
                        self.board[i][j] = self.game.o_label
                        score = self._minimax(alpha, beta, depth + 1, False)
                        self.board[i][j] = " "
                        best_score = max(score, best_score)
                        alpha = max(alpha, score)

                        if beta <= alpha:
                            break
            return best_score
        else:
            best_score = float("inf")

            for i in range(self.game.rows):
                for j in range(self.game.cols):
                    if self.board[i][j] == " ":
                        self.board[i][j] = self.game.x_label
                        score = self._minimax(alpha, beta, depth + 1, True)
                        self.board[i][j] = " "
                        best_score = min(score, best_score)
                        beta = min(beta, score)

                        if beta <= alpha:
                            break
            return best_score
