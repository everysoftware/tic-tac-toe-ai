from .ai import AIMechanic
from .two_players import TwoPlayersMechanic

mechanic_list = [
    (TwoPlayersMechanic, "с другим игроком"),
    (AIMechanic, "с компьютером"),
]

__all__ = ("AIMechanic", "TwoPlayersMechanic", "mechanic_list")
