from .color import Color
from .move import Move
from .pieces.pawn import Pawn
from .pieces.rook import Rook
from .pieces.knight import Knight
from .pieces.bishop import Bishop
from .pieces.king import King
from .pieces.queen import Queen
from .pieces.constants import Pieces
from copy import deepcopy

BOARD_DIMENSION = 8

class Board:
  def __init__(self):
    self.board = [[None for x in range(BOARD_DIMENSION)] for x in range(BOARD_DIMENSION)]
    self.previous_move = None
    self.init_board()

  def is_position_in_bounds(self, position):
    return all(position[x] >= 0 and position[x] < BOARD_DIMENSION for x in [0, 1])

  def get(self, position):
    try:
      return self.board[position[0]][position[1]]
    except:
      return None

  def get_pieces(self, color):
    pieces = []
    for file in self.board:
      for piece in file:
        if piece is not None and piece.get_color() is color:
          pieces.append(piece)
    return pieces

  def get_king(self, color):
    pieces = self.get_pieces(color)
    return next((piece for piece in pieces if piece.get_name() == Pieces.KING))

  def get_previous_move(self):
    return self.previous_move

  def is_position_empty(self, position):
    return self.get(position) is None

  def is_color_at_position_attacked(self, color, position):
    opposing_pieces = self.get_pieces(Color.WHITE if color == Color.BLACK else Color.BLACK)
    valid_moves = []
    for opposing_piece in opposing_pieces:
      valid_moves += opposing_piece.get_valid_moves()
    check_moves = [valid_move for valid_move in valid_moves if valid_move.get_new_position() == position]
    if len(check_moves) > 0:
      print(check_moves[0])
    return any(valid_move.get_new_position() == position for valid_move in valid_moves)

  def handle_move(self, move):
    # confirm that this move's piece is actually on the board
    if move.get_piece() not in self.get_pieces(move.get_piece().get_color()):
      return False
    valid_moves = move.piece.get_valid_moves()
    try:
      valid_move = next(m for m in valid_moves if m.new_position == move.new_position)
    except StopIteration:
      print('ERROR: Invalid move.')
      return False
    if self.is_castle_through_check(move):
      print('Attempting to castle through check, thus invalid')
      return False
    old_board = deepcopy(self.board)
    old_position = valid_move.get_piece().get_position()
    new_position = valid_move.get_new_position()
    valid_move.piece.set_position(new_position)
    self.board[old_position[0]][old_position[1]] = None
    if valid_move.get_promoting_to() is not None:
      self.board[new_position[0]][new_position[1]] = valid_move.get_promoting_to()
    else:
      self.board[new_position[0]][new_position[1]] = valid_move.piece
    self.handle_castle(move.get_castling_with(), old_position)
    moving_color = move.get_piece().get_color()
    if self.is_color_at_position_attacked(moving_color, self.get_king(moving_color).get_position()):
      print('Move results in check, thus invalid')
      self.board = old_board
      return False
    previous_move = move
    return True

  def is_castle_through_check(self, move):
    king_position = move.get_piece().get_position()
    castling_with = move.get_castling_with()
    if castling_with is None:
      return False
    direction = -1 if castling_with.get_position()[0] < king_position[0] else 1
    king_positions = [king_position, (king_position[0] + direction, king_position[1]), (king_position[0] + direction * 2, king_position[1])]
    return any(self.is_color_at_position_attacked(move.get_piece().get_color(), position) for position in king_positions)

  def handle_castle(self, castling_with, old_king_position):
    if castling_with is None:
      return
    direction = -1 if castling_with.get_position()[0] < old_king_position[0] else 1
    old_rook_position = castling_with.get_position()
    new_rook_position = (old_king_position[0] + direction, old_king_position[1])
    castling_with.set_position(new_rook_position)
    self.board[old_rook_position[0]][old_rook_position[1]] = None
    self.board[new_rook_position[0]][new_rook_position[1]] = castling_with

  def init_board(self):
    for index, file in enumerate(self.board):
      file[1] = Pawn(board=self, position=(index, 1), color=Color.WHITE)
      file[6] = Pawn(board=self, position=(index, 6), color=Color.BLACK)
      if index == 0 or index == 7:
        file[0] = Rook(board=self, position=(index, 0), color=Color.WHITE)
        file[7] = Rook(board=self, position=(index, 7), color=Color.BLACK)
      if index == 1 or index == 6:
        file[0] = Knight(board=self, position=(index, 0), color=Color.WHITE)
        file[7] = Knight(board=self, position=(index, 7), color=Color.BLACK)
      if index == 2 or index == 5:
        file[0] = Bishop(board=self, position=(index, 0), color=Color.WHITE)
        file[7] = Bishop(board=self, position=(index, 7), color=Color.BLACK)
      if index == 3:
        file[0] = Queen(board=self, position=(index, 0), color=Color.WHITE)
        file[7] = King(board=self, position=(index, 7), color=Color.BLACK)
      if index == 4:
        file[0] = King(board=self, position=(index, 0), color=Color.WHITE)
        file[7] = Queen(board=self, position=(index, 7), color=Color.BLACK)

  def __str__(self):
    out = ''
    for rank_index in reversed(range(BOARD_DIMENSION)):
      line = ''
      for file in self.board:
        piece = file[rank_index]
        color = Colors.WHITE if piece is None or piece.get_color() is Color.WHITE else Colors.BLACK
        line += color + '{:<15}'.format(str(piece)) + Colors.ENDC if piece is not None else '{:<15}'.format(str(piece))
      line += '\n' * 4
      out += line
    return out

class Colors:
    BLACK = '\033[30m'
    WHITE = '\033[90m'
    ENDC = '\033[0m'
