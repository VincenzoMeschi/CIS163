from chess_piece import ChessPiece
from move import Move
from typing import List
from player import Player


class Bishop(ChessPiece):
    
    def __str__(self) -> str:
        return "B"
    
    def type(self) -> str:
        return "bishop"
    
    def is_valid_move(self, move: Move, board: List[List["ChessPiece"]]) -> bool:
        if not super().is_valid_move(move, board):
            return False
        
        # If the bishop is moving diagonally
        if abs(move.from_row - move.to_row) == abs(move.from_col - move.to_col):
            # If the bishop is moving to the upper right
            if move.from_row > move.to_row and move.from_col < move.to_col:
                # If the path is clear and the destination is empty or occupied by the other player
                if board[move.to_row][move.to_col] is None or board[move.to_row][move.to_col].player != self.player:
                    for i in range(1, abs(move.from_row - move.to_row)):
                        if board[move.from_row - i][move.from_col + i] is not None:
                            return False
                    return True
            # If the bishop is moving to the upper left
            if move.from_row > move.to_row and move.from_col > move.to_col:
                # If the path is clear and the destination is empty or occupied by the other player
                if board[move.to_row][move.to_col] is None or board[move.to_row][move.to_col].player != self.player:
                    for i in range(1, abs(move.from_row - move.to_row)):
                        if board[move.from_row - i][move.from_col - i] is not None:
                            return False
                    return True
            # If the bishop is moving to the lower right
            if move.from_row < move.to_row and move.from_col < move.to_col:
                # If the path is clear and the destination is empty or occupied by the other player
                if board[move.to_row][move.to_col] is None or board[move.to_row][move.to_col].player != self.player:
                    for i in range(1, abs(move.from_row - move.to_row)):
                        if board[move.from_row + i][move.from_col + i] is not None:
                            return False
                    return True
            # If the bishop is moving to the lower left
            if move.from_row < move.to_row and move.from_col > move.to_col:
                # If the path is clear and the destination is empty or occupied by the other player
                if board[move.to_row][move.to_col] is None or board[move.to_row][move.to_col].player != self.player:
                    for i in range(1, abs(move.from_row - move.to_row)):
                        if board[move.from_row + i][move.from_col - i] is not None:
                            return False
                    return True
        return False