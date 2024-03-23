from abc import ABC, abstractmethod
from player import Player
from move import Move
from typing import List


class ChessPiece(ABC):

    def __init__(self, player: Player) -> None:
        self.__player = player

    @property
    def player(self) -> Player:
        return self.__player

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def type(self) -> str:
        pass

    def is_valid_move(self, move: Move, board: List[List["ChessPiece"]]) -> bool:
        # Check if either to_row or to_col is None
        if move.to_row is None or move.to_col is None:
            return False

        # Makes sure the initial piece is within the bounds of the board
        if (
                move.to_row < 0
                or move.to_row > 7
                or move.to_col < 0
                or move.to_col > 7
        ):
            return False

        # Makes sure the final move is within the bounds of the board
        if (
            move.to_row < 0
            or move.to_row > 7
            or move.to_col < 0
            or move.to_col > 7
        ):
            return False

        # Makes sure the initial and final moves are different
        if move.from_row == move.to_row and move.from_col == move.to_col:
            return False

        # Makes sure the initial piece moves to a location other than start
        if board[move.from_row][move.from_col] != self:
            return False

        # Makes sure the final location does not contain a piece belonging to the same player
        if (
            board[move.to_row][move.to_col] is not None
            and board[move.to_row][move.to_col].player == self.player
        ):
            return False

        # If all the above conditions are met, the move is valid
        return True
