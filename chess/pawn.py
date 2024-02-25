from chess_piece import ChessPiece
from move import Move
from typing import List


class Pawn(ChessPiece):

    def __str__(self) -> str:
        return "P"

    def type(self) -> str:
        return "pawn"

    def is_valid_move(self, move: Move, board: List[List["ChessPiece"]]) -> bool:
        if not super().is_valid_move(move, board):
            return False

        # If the pawn is white
        if self.player == 0:
            # if pawn is moving forward and not taking
            if move.from_col == move.to_col:
                # if pawn is moving forward 1 space
                if move.to_row - move.from_row == -1:
                    # if the space is empty
                    if board[move.to_row][move.to_col] is None:
                        return True
                # if pawn is moving forward 2 spaces
                elif move.from_row == 6 and move.to_row == 4:
                    # if the space is empty
                    if (
                        board[move.to_row][move.to_col] is None
                        and board[move.to_row + 1][move.to_col] is None
                    ):
                        return True

                # if pawn is taking
                if (
                    abs(move.from_col - move.to_col) == 1
                    and move.from_row - move.to_row == 1
                ):
                    # if the piece belongs to the other player
                    if (
                        board[move.to_row][move.to_col] is not None
                        and board[move.to_row][move.to_col].player == 1
                    ):
                        return True

        # If the pawn is black
        elif self.player == 1:
            # if pawn is moving forward and not taking
            if move.from_col == move.to_col:
                # if pawn is moving forward 1 space
                if move.to_row - move.from_row == 1:
                    # if the space is empty
                    if board[move.to_row][move.to_col] is None:
                        return True
                # if pawn is moving forward 2 spaces
                elif move.from_row == 1 and move.to_row == 3:
                    # if the space is empty
                    if (
                        board[move.to_row][move.to_col] is None
                        and board[move.to_row - 1][move.to_col] is None
                    ):
                        return True
            # if pawn is taking
            elif (
                abs(move.from_col - move.to_col) == 1
                and move.to_row - move.from_row == 1
            ):
                # if the piece belongs to the other player
                if (
                    board[move.to_row][move.to_col] is not None
                    and board[move.to_row][move.to_col].player == 0
                ):
                    return True

        return False
