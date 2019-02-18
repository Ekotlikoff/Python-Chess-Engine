from ..color import Color
from ..move import Move
from .piece import Piece
from .constants import Pieces

class Knight(Piece):
  def __init__(self, **kwargs):
    super().__init__(**kwargs, name=Pieces.KNIGHT)
    self.valid_hop_vectors = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

  def get_moves(self):
    valid_moves = []
    vectors = self.valid_hop_vectors
    for vector in vectors:
      new_position = (self.position[0] + vector[0], self.position[1] + vector[1])
      if self.get_board().is_position_in_bounds(new_position) and self.get_board().is_position_empty(new_position):
        valid_moves.append(Move(self, new_position, False))
      elif self.get_board().is_position_in_bounds(new_position) and self.get_board().get(new_position).color is not self.color:
        valid_moves.append(Move(self, new_position, True, capturing_position=new_position))
    return valid_moves
