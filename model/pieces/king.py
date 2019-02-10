from ..color import Color
from ..move import Move
from .piece import Piece
from .constants import Pieces

class King(Piece):
  def __init__(self, **kwargs):
    super().__init__(**kwargs, name=Pieces.KING)
    self.valid_slide_vectors = [(1, 1), (-1, 1), (1, -1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]

  def get_valid_moves(self):
    valid_moves = self.get_valid_moves_slide(max_slide_length=1)
    if not self.has_piece_moved():
      rooks = [piece for piece in self.get_board().get_pieces(self.color) if piece.get_name() == Pieces.ROOK]
      for rook in rooks:
        if self.can_castle(rook):
          direction = -2 if rook.get_position()[0] < self.get_position()[0] else 2
          new_position = (self.get_position()[0] + direction, self.get_position()[1])
          valid_moves.append(Move(self, new_position, False, castling_with=rook))
    return valid_moves

  def can_castle(self, rook):
    return not rook.has_piece_moved() and any(abs(move.get_new_position()[0] - self.get_position()[0]) == 1 for move in rook.get_valid_moves())
