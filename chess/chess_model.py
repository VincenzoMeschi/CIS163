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


class ChessModel:
    def __init__(self, board: List[List["ChessPiece"]], player: Player, nrows: int, ncols: int, message_code: MoveValidity):
        self.board = board
        self.__player = player
        self.__nrows = nrows
        self.__ncols = ncols
        self.__message_code = message_code
        
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
        pass
    
    
    def is_valid_move(self, move: Move) -> bool:
        piece = self.board[move.from_row][move.from_col]
        if piece == None:
            return False
        if piece.player != self.current_player:
            return False
        if not piece.is_valid_move(self, move):
            return False
        
        
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
        self.board[move.to_row][move.to_col] = self.board[move.from_row][move.from_col]
        self.board[move.from_row][move.from_col] = None
        self.set_next_player()
    
    # Identifies if the player is in check based on the current state of the board
    def in_check(self, player: Player) -> bool:
        if player == Player.WHITE:
            king = King(Player.WHITE)
        else:
            king = King(Player.BLACK)
            
        for row in range(self.nrows):
            for col in range(self.ncols):
                piece = self.board[row][col]
                if piece == king:
                    king_row = row
                    king_col = col
                    break
                
        for row in range(self.nrows):
            for col in range(self.ncols):
                piece = self.board[row][col]
                if piece != None and piece.player != player:
                    if piece.is_valid_move(self, Move(row, col, king_row, king_col)):
                        return True
                    
        return False
    
    # ChessPiece method -> returns the piece at the given row and col
    def piece_at(self, row: int, col: int) -> ChessPiece:
        if row < 0 or row >= self.nrows or col < 0 or col >= self.ncols:
            raise ValueError("Row and col are out of bounds.")
        
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
        pass
        
        
        
class UndoException(Exception):
    pass

    
    
        
        

        