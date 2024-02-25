from enum import Enum
from player import Player
from move import Move

# from chess_piece import ChessPiece
# from pawn import Pawn
# from rook import Rook
# from knight import Knight
# from bishop import Bishop
# from queen import Queen
# from king import King
# from move import Move


class MoveValidity(Enum):
    Valid = 1
    Invalid = 2
    MovingIntoCheck = 3
    StayingInCheck = 4

    def __str__(self):
        if self.value == 2:
            return "Invalid move."

        if self.value == 3:
            return "Invalid -- cannot move into check."

        if self.value == 4:
            return "Invalid -- must move out of check."


# TODO: create UndoException


class ChessModel:
    pass


class UndoException(Exception):
    pass
