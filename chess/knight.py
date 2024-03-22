from chess_piece import ChessPiece
from move import Move
from typing import List
from player import Player


class Knight(ChessPiece):
    
    def __str__(self) -> str:
        return "N"
    
    def type(self) -> str:
        return "Knight"
    
    def is_valid_move(self, move: Move, board: List[List["ChessPiece"]]) -> bool:
        if not super().is_valid_move(move, board):
            return False
        
        # If the knight is moving in an L shape
        if (
            abs(move.from_row - move.to_row) == 2
            and abs(move.from_col - move.to_col) == 1
        ) or (
            abs(move.from_row - move.to_row) == 1
            and abs(move.from_col - move.to_col) == 2
        ):
            # If knight's destination is empty or occupied by the other player
            if (
                board[move.to_row][move.to_col] is None
                or board[move.to_row][move.to_col].player != self.player
            ):
                return True
        
        return False