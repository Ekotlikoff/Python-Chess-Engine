from ..color import Color
from ..move import Move
from .piece import Piece
from .constants import Pieces

class Bishop(Piece):
  def __init__(self, **kwargs):
    super().__init__(**kwargs, name=Pieces.BISHOP)
    self.valid_slide_vectors = [(1, 1), (-1, 1), (1, -1), (-1, -1)]

  def get_moves(self):
    return self.get_valid_moves_slide()
