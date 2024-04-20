from src.mechanics.base import MechanicBase


class AIMechanic(MechanicBase):
    def __init__(self, game):
        super().__init__(game)

    def make_move(self) -> None:
        if self.game.logic.current_player == self.game.x_label:
            return

        best_score = float("-inf")
        move = None

        depth = 0
        while True:
            for i in range(self.game.rows):
                for j in range(self.game.cols):
                    if self.board[i][j] == " ":
                        self.board[i][j] = self.game.logic.current_player
                        score = self._minimax(
                            0, depth, float("-inf"), float("inf"), False
                        )
                        self.board[i][j] = " "

                        if score > best_score:
                            best_score = score
                            move = (i, j)

            if move is not None:
                break

            depth += 1

        self.game.gui.process_move(*move)

    def _minimax(
        self,
        current_depth: int,
        max_depth: int,
        alpha: float,
        beta: float,
        is_maximizing: bool,
    ) -> int:
        if self.check_win():
            return 1 if self.game.logic.current_player == self.game.o_label else -1
        elif self.check_draw():
            return 0
        elif current_depth == max_depth:
            return 0

        if is_maximizing:
            best_score = float("-inf")

            for i in range(self.game.rows):
                for j in range(self.game.cols):
                    if self.board[i][j] == " ":
                        self.board[i][j] = self.game.o_label
                        score = self._minimax(
                            current_depth + 1, max_depth, alpha, beta, False
                        )
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
                        score = self._minimax(
                            current_depth + 1, max_depth, alpha, beta, True
                        )
                        self.board[i][j] = " "
                        best_score = min(score, best_score)
                        beta = min(beta, score)

                        if beta <= alpha:
                            break
            return best_score
