from chess_piece import ChessPiece
from move import Move
from typing import List
from player import Player


class Queen(ChessPiece):
    
    def __str__(self) -> str:
        return "Q"
    
    def type(self) -> str:
        return "Queen"
    
    def is_valid_move(self, move: Move, board: List[List[ChessPiece]]) -> bool:
        if not super().is_valid_move(move, board):
            return False
        
        # If the queen is moving horizontally
        if move.from_row == move.to_row:
            # If the queen is moving to the right
            if move.from_col < move.to_col:
                # If the path is clear and the destination is empty or occupied by the other player
                for col in range(move.from_col + 1, move.to_col):
                    if board[move.from_row][col] is not None:
                        return False
                if (
                    board[move.to_row][move.to_col] is None
                    or board[move.to_row][move.to_col].player != self.player
                ):
                    return True
            # If the queen is moving to the left
            elif move.from_col > move.to_col:
                # If the path is clear and the destination is empty or occupied by the other player
                for col in range(move.to_col + 1, move.from_col):
                    if board[move.from_row][col] is not None:
                        return False
                if (
                    board[move.to_row][move.to_col] is None
                    or board[move.to_row][move.to_col].player != self.player
                ):
                    return True
        
        # If the queen is moving vertically
        elif move.from_col == move.to_col:
            # If the queen is moving upwards
            if move.from_row > move.to_row:
                # If the path is clear and the destination is empty or occupied by the other player
                for row in range(move.to_row + 1, move.from_row):
                    if board[row][move.from_col] is not None:
                        return False
                if (
                    board[move.to_row][move.to_col] is None
                    or board[move.to_row][move.to_col].player != self.player
                ):
                    return True
            # If the queen is moving downwards
            elif move.from_row < move.to_row:
                # If the path is clear and the destination is empty or occupied by the other player
                for row in range(move.from_row + 1, move.to_row):
                    if board[row][move.from_col] is not None:
                        return False
                if (
                    board[move.to_row][move.to_col] is None
                    or board[move.to_row][move.to_col].player != self.player
                ):
                    return True
                
        # If the queen is moving diagonally
        if abs(move.from_row - move.to_row) == abs(move.from_col - move.to_col):
            # If the queen is moving to the upper right
            if move.from_row > move.to_row and move.from_col < move.to_col:
                # If the path is clear and the destination is empty or occupied by the other player
                if board[move.to_row][move.to_col] is None or board[move.to_row][move.to_col].player != self.player:
                    for i in range(1, abs(move.from_row - move.to_row)):
                        if board[move.from_row - i][move.from_col + i] is not None:
                            return False
                    return True
            # If the queen is moving to the upper left
            if move.from_row > move.to_row and move.from_col > move.to_col:
                # If the path is clear and the destination is empty or occupied by the other player
                if board[move.to_row][move.to_col] is None or board[move.to_row][move.to_col].player != self.player:
                    for i in range(1, abs(move.from_row - move.to_row)):
                        if board[move.from_row - i][move.from_col - i] is not None:
                            return False
                    return True
            # If the queen is moving to the lower right
            if move.from_row < move.to_row and move.from_col < move.to_col:
                # If the path is clear and the destination is empty or occupied by the other player
                if board[move.to_row][move.to_col] is None or board[move.to_row][move.to_col].player != self.player:
                    for i in range(1, abs(move.from_row - move.to_row)):
                        if board[move.from_row + i][move.from_col + i] is not None:
                            return False
                    return True
            # If the queen is moving to the lower left
            if move.from_row < move.to_row and move.from_col > move.to_col:
                # If the path is clear and the destination is empty or occupied by the other player
                if board[move.to_row][move.to_col] is None or board[move.to_row][move.to_col].player != self.player:
                    for i in range(1, abs(move.from_row - move.to_row)):
                        if board[move.from_row + i][move.from_col - i] is not None:
                            return False
                    return True
        return False