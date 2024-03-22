from enum import Enum
from player import Player
from move import Move
from chess_piece import ChessPiece
from pawn import Pawn
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King
from move import Move

from typing import List


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


class UndoException(Exception):
    pass


class ChessModel:
    def __init__(self):
        self.__player = Player.WHITE

        self.__nrows = 8
        self.__ncols = 8
        self.board = [[None] * self.__ncols for _ in range(self.__nrows)]

        self.__message_code = None

        self.__history = []
        self.temp_board = []

        self.set_piece(0, 0, Rook(Player.BLACK))
        self.set_piece(0, 1, Knight(Player.BLACK))
        self.set_piece(0, 2, Bishop(Player.BLACK))
        self.set_piece(0, 3, Queen(Player.BLACK))
        self.set_piece(0, 4, King(Player.BLACK))
        self.set_piece(0, 5, Bishop(Player.BLACK))
        self.set_piece(0, 6, Knight(Player.BLACK))
        self.set_piece(0, 7, Rook(Player.BLACK))
        for col in range(8):
            self.set_piece(1, col, Pawn(Player.BLACK))

        self.set_piece(7, 0, Rook(Player.WHITE))
        self.set_piece(7, 1, Knight(Player.WHITE))
        self.set_piece(7, 2, Bishop(Player.WHITE))
        self.set_piece(7, 3, Queen(Player.WHITE))
        self.set_piece(7, 4, King(Player.WHITE))
        self.set_piece(7, 5, Bishop(Player.WHITE))
        self.set_piece(7, 6, Knight(Player.WHITE))
        self.set_piece(7, 7, Rook(Player.WHITE))
        for col in range(8):
            self.set_piece(6, col, Pawn(Player.WHITE))

    @property
    def nrows(self):
        return self.__nrows

    @property
    def ncols(self):
        return self.__ncols

    @property
    def current_player(self):
        return self.__player

    @property
    def messageCode(self):
        return self.__message_code

    # Check to see if current player is checkmated or stuck
    def is_complete(self) -> bool:
        for row in range(self.__nrows):
            for col in range(self.__ncols):
                piece = self.board[row][col]
                if piece and piece.player == self.__player:
                    for to_row in range(self.__nrows):
                        for to_col in range(self.__ncols):
                            move = Move(row, col, to_row, to_col)
                            if self.is_valid_move(move):
                                return False
        return True if self.in_check(self.__player) else False

    def is_valid_move(self, move: Move) -> bool:
        piece = self.board[move.from_row][move.from_col]
        if piece == None:
            self.__message_code = MoveValidity.Invalid
            return False
        if piece.player != self.current_player:
            self.__message_code = MoveValidity.Invalid
            return False
        if not piece.is_valid_move(move, self.board):
            self.__message_code = MoveValidity.Invalid
            return False
        
        if self.is_complete():
          return

        # If the player is currently in check
        if self.in_check(self.current_player):
            # Make the move
            self.move(move)

            # If the player is still in check after the move, undo the move and return False
            if self.in_check(self.current_player):
                self.undo()
                self.__message_code = MoveValidity.StayingInCheck
                return False
        else:
            # If the player is not in check, make the move and check if the player is now in check
            self.move(move)

            # If the player is now in check, undo the move and return False
            if self.in_check(self.current_player):
                self.undo()
                self.__message_code = MoveValidity.MovingIntoCheck
                return False

        self.undo()
        self.__message_code = MoveValidity.Valid
        return True

    # Carries out move that is given in the move object
    def move(self, move: Move):
        capture = self.board[move.to_row][move.to_col]
        self.board[move.to_row][move.to_col] = self.board[move.from_row][move.from_col]
        self.board[move.from_row][move.from_col] = None
        self.__history.append((move, capture))
        self.set_next_player()

    # Identifies if the player is in check based on the current state of the board
    def in_check(self, player: Player) -> bool:
        if player == Player.WHITE:
            king = King(Player.WHITE)
        else:
            king = King(Player.BLACK)

        king_row = None
        king_col = None
        for row in range(self.nrows):
            for col in range(self.ncols):
                piece = self.board[row][col]
                if isinstance(piece, King):
                    king_row = row
                    king_col = col
                    break

        for row in range(self.nrows):
            for col in range(self.ncols):
                piece = self.board[row][col]
                if piece is not None and piece.player != player:
                    if piece.is_valid_move(
                        Move(row, col, king_row, king_col), self.board
                    ):
                        return True

        return False

    # ChessPiece method -> returns the piece at the given row and col
    def piece_at(self, row: int, col: int) -> ChessPiece:
        return self.board[row][col]

    def set_next_player(self):
        if self.current_player == Player.WHITE:
            self.__player = Player.BLACK
        else:
            self.__player = Player.WHITE

    # Check if row and col are in bounds, raiase a  ValueError if not
    # make sure that a piece is a ChessPiece. if not, raise a TypeError
    def set_piece(self, row: int, col: int, piece: ChessPiece):
        if row < 0 or row >= self.nrows or col < 0 or col >= self.ncols:
            raise ValueError("Row and col are out of bounds.")

        if not isinstance(piece, ChessPiece):
            raise TypeError("Piece is not a ChessPiece.")

        self.board[row][col] = piece

    # Allow multiple undos
    # if called and no undos can be made, raise an UndoException (create a class)
    #     undo(self) method: undoes the most-recent move that has not yet been undone.
    # This method should work to allow mutiple undos (aka, if you call the undo method twice, it should remove the most recent move and the move prior to that one).
    # In the chess_model.py file, but outside of your ChessModel class, create a class called UndoException which inherits from Exception
    # If the undo method is called when there are no moves left to undo, raise an UndoException (the GUI is already designed to handle this).
    def undo(self):
        if len(self.__history) == 0:
            raise UndoException("No moves to undo!")

        while len(self.__history) > 0:
            prev, capture = self.__history.pop()
            moved_piece = self.board[prev.to_row][prev.to_col]
            self.board[prev.to_row][prev.to_col] = capture
            self.board[prev.from_row][prev.from_col] = moved_piece
            if moved_piece is not None and moved_piece.player != self.current_player:
                break
        self.set_next_player()


class UndoException(Exception):
    pass
