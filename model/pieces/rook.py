from ..color import Color
from .piece import Piece
from .constants import Pieces

class Rook(Piece):
  def __init__(self, **kwargs):
    super().__init__(**kwargs, name=Pieces.ROOK)
    self.can_castle = True
    self.valid_slide_vectors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

  def get_moves(self):
    return self.get_valid_moves_slide()
