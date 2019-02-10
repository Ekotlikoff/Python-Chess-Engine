from ..color import Color
from .piece import Piece
from .constants import Pieces

class Queen(Piece):
  def __init__(self, **kwargs):
    super().__init__(**kwargs, name=Pieces.QUEEN)
    self.valid_slide_vectors = [(1, 1), (-1, 1), (1, -1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]

  def get_valid_moves(self):
    return self.get_valid_moves_slide()
