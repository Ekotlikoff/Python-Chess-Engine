from ..color import Color
from ..move import Move
from .piece import Piece
from .queen import Queen
from .knight import Knight
from .constants import Pieces
from copy import deepcopy

class Pawn(Piece):
  def __init__(self, **kwargs):
    super().__init__(**kwargs, name=Pieces.PAWN)
    self.valid_slide_vectors = [(0, self.color.value)]

  def get_valid_moves(self):
    max_slide_length = 1 if self.has_moved else 2
    valid_moves = self.get_valid_moves_slide(max_slide_length=max_slide_length, can_attack=False)
    attacking_positions = [(self.position[0] + x, self.position[1] + self.color.value) for x in [1, -1]]
    attacking_positions = [pos for pos in attacking_positions if self.board.is_position_in_bounds(pos)]
    for attacked_piece in [self.board.get(position) for position in attacking_positions]:
      if attacked_piece is not None and attacked_piece.color is not self.color:
        valid_moves.append(Move(self, attacked_piece.get_position(), True))
    try:
      promoting_moves = [move for move in valid_moves if move.get_new_position()[1] == 0 or move.get_new_position()[1] == 7]
      for promoting_move in promoting_moves:
        new_piece = self.get_promoting_piece(promoting_move)
        new_knight_piece = self.get_promoting_knight_piece(promoting_move)
        promoting_move.set_promoting_to(new_piece)
        knight_promoting_move = deepcopy(promoting_move)
        knight_promoting_move.set_promoting_to(new_knight_piece)
        valid_moves.append(knight_promoting_move)
    except Exception as e:
      print(e)
    except:
      pass
    return valid_moves

  def get_promoting_piece(self, promoting_move):
    return Queen(board=self.get_board(), position=promoting_move.get_new_position(), color=self.get_color())

  def get_promoting_knight_piece(self, promoting_move):
    return Knight(board=self.get_board(), position=promoting_move.get_new_position(), color=self.get_color())
