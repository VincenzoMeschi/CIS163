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














class MoveValidity(Enum):
  Valid = 1
  Invalid = 2
  MovingIntoCheck = 3
  StayingInCheck = 4




  def __str__(self):
      if self.value == 1:
          return "Valid move."
      elif self.value == 2:
          return "Invalid move."
      elif self.value == 3:
          return "Invalid -- cannot move into check."
      elif self.value == 4:
          return "Invalid -- must move out of check."
      else:
          return "Unknown move validity."








class ChessModel:
  def __init__(self):
      self.__nrows = 8
      self.__ncols = 8
      self.__player = Player.WHITE
      self.__message_code = MoveValidity.Valid
      self.board = [[None] * self.__ncols for _ in range(self.__nrows)]
      self.setup_standard_board()
      self.move_history = []
      self.temp_board = None




  def setup_standard_board(self):
      # Set up pawns
  #This works. just commented for testing
      for col in range(self.ncols):
          self.set_piece(1, col, Pawn(Player.BLACK))
          self.set_piece(self.nrows - 2, col, Pawn(Player.WHITE))




      # Set up other pieces
      self.set_piece(0, 0, Rook(Player.BLACK))
      self.set_piece(0, 1, Knight(Player.BLACK))
      self.set_piece(0, 2, Bishop(Player.BLACK))
      self.set_piece(0, 3, Queen(Player.BLACK))
      self.set_piece(0, 4, King(Player.BLACK))
      self.set_piece(0, 5, Bishop(Player.BLACK))
      self.set_piece(0, 6, Knight(Player.BLACK))
      self.set_piece(0, 7, Rook(Player.BLACK))




      self.set_piece(7, 0, Rook(Player.WHITE))
      self.set_piece(7, 1, Knight(Player.WHITE))
      self.set_piece(7, 2, Bishop(Player.WHITE))
      self.set_piece(7, 3, Queen(Player.WHITE))
      self.set_piece(7, 4, King(Player.WHITE))
      self.set_piece(7, 5, Bishop(Player.WHITE))
      self.set_piece(7, 6, Knight(Player.WHITE))
      self.set_piece(7, 7, Rook(Player.WHITE))

  @property
  def nrows(self) -> int:
      return self.__nrows

  @property
  def ncols(self) -> int:
      return self.__ncols

  @property
  def current_player(self) -> Player:
      return self.__player

  @property
  def messageCode(self) -> MoveValidity:
      return self.__message_code

  @nrows.setter
  def nrows(self, value: int):
      self.__nrows = value

  @ncols.setter
  def ncols(self, value: int):
      self.__ncols = value

  @current_player.setter
  def current_player(self, value: Player):
      self.__player = value

  @messageCode.setter
  def messageCode(self, value: MoveValidity):
      self.__message_code = value


  def is_valid_move(self, move: Move) -> bool:
      piece = self.board[move.from_row][move.from_col]
      if piece is None or not isinstance(piece, ChessPiece) or piece.player != self.__player:
          self.__message_code = MoveValidity.Invalid
          return False

      if not piece.is_valid_move(move, self.board):
          self.__message_code = MoveValidity.Invalid
          return False


      # Simulate the move to check for moving into check
      simulated_board = []
      for row in self.board:
          simulated_row = []
          for item in row:
              simulated_row.append(item)
          simulated_board.append(simulated_row)

      simulated_board[move.to_row][move.to_col] = piece
      simulated_board[move.from_row][move.from_col] = None
      if self.in_check(self.__player, simulated_board):
          self.__message_code = MoveValidity.MovingIntoCheck
          return False


      self.__message_code = MoveValidity.Valid
      return True
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


  def move(self, move: Move):
      # Check if the game is already in checkmate
      if self.is_complete():
          return

      # Make a copy of the current board state
      current_state = [row[:] for row in self.board]

      # Make the move on the board
      self.board[move.to_row][move.to_col] = self.board[move.from_row][move.from_col]
      self.board[move.from_row][move.from_col] = None


      # Check for pawn promotion to Queen
      moved_piece = self.piece_at(move.to_row, move.to_col)
      if isinstance(moved_piece, Pawn) and (
              (moved_piece.player == Player.WHITE and move.to_row == 0) or
              (moved_piece.player == Player.BLACK and move.to_row == 7)
      ):
          # Promote the pawn to a Queen
          promoted_piece = Queen(moved_piece.player)
          self.board[move.to_row][move.to_col] = promoted_piece

      # Set the next player
      self.set_next_player()

      # Save the move and the recorded board state to the move history
      self.move_history.append((current_state, move))

  def in_check(self, player: Player, board=None):
      if board is None:
          board = self.board


      king_row, king_col = None, None
      for row in range(self.__nrows):
          for col in range(self.__ncols):
              piece = board[row][col]
              if isinstance(piece, King) and piece.player == player:
                  king_row, king_col = row, col
                  break
          if king_row is not None:
              break

      if king_row is None or king_col is None:
          return False

      for row in range(self.__nrows):
          for col in range(self.__ncols):
              piece = board[row][col]
              if piece and piece.player != player:
                  move = Move(row, col, king_row, king_col)
                  if piece.is_valid_move(move, board):
                      return True
      return False


  # ChessPiece method -> returns the piece at the given row and col
  def piece_at(self, row: int, col: int) -> ChessPiece:
      # Return None if coordinates are out of bounds
      if not (0 <= row < self.nrows) or not (0 <= col < self.ncols):
          return None

      piece = self.board[row][col]

      if piece is None:
          return None

      if not isinstance(piece, ChessPiece):
          raise TypeError("Invalid piece found at the specified location.")
      return piece


  def set_next_player(self):
      if self.current_player == Player.WHITE:
          self.__player = Player.BLACK
      else:
          self.__player = Player.WHITE


  # Check if row and col are in bounds, raiase a  ValueError if not
  # make sure that a piece is a ChessPiece. if not, raise a TypeError
  def set_piece(self, row: int, col: int, piece: ChessPiece):
      if row < 0 or row >= self.__nrows or col < 0 or col >= self.__ncols:
          raise ValueError("Row and col are out of bounds.")

      if not (piece is None or isinstance(piece, ChessPiece)):
          raise TypeError("Piece is not a ChessPiece.")

      self.board[row][col] = piece



  def undo(self):
      if not self.move_history:
          raise UndoException("No moves to undo")

      # Retrieve the last move and board state from the history
      last_state, last_move = self.move_history.pop()

      # Restore the previous board state using deep copy
      self.board = []
      for row in last_state:
          self.board.append(row[:])

      # Switch back to the player who made the undone move
      self.set_next_player()




class UndoException(Exception):
  def __init__(self, message="No moves left to undo"):
      self.message = message
      super().__init__(self.message)
