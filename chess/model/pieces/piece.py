from ..move import Move
from ..color import Color

class Piece:
  def __init__(self, board=None, position=None, color=None, name=None):
    if board is None:
      raise TypeError("position may not be None")
    if position is None:
      raise TypeError("position may not be None")
    if color is None:
      raise TypeError("color may not be None")
    if name is None:
      raise TypeError("name may not be None")
    
    self.board = board
    self.position = position
    self.color = color
    self.has_moved = False
    self.name = name

  def get_position(self):
    return self.position

  def get_name(self):
    return self.name

  def get_color(self):
    return self.color

  def get_board(self):
    return self.board

  def has_piece_moved(self):
    return self.has_moved

  def set_position(self, new_position):
    self.position = new_position
    self.has_moved = True

  def get_valid_moves_slide(self, max_slide_length=None, can_attack=True):
    valid_moves = []
    vectors = self.valid_slide_vectors
    for vector in vectors:
      new_position = (self.position[0] + vector[0], self.position[1] + vector[1])
      current_slide_length = 1
      while self.can_move_without_taking(new_position, current_slide_length, max_slide_length):
        valid_moves.append(Move(self, new_position, False))
        new_position = (new_position[0] + vector[0], new_position[1] + vector[1])
        current_slide_length += 1
      if can_attack and self.can_slide(current_slide_length, max_slide_length) and self.board.is_position_in_bounds(new_position) and self.board.get(new_position).color is not self.color:
        valid_moves.append(Move(self, new_position, True))
    return valid_moves

  def can_move_without_taking(self, new_position, current_slide_length, max_slide_length):
    return self.board.is_position_in_bounds(new_position) and self.board.is_position_empty(new_position) and self.can_slide(current_slide_length, max_slide_length)

  def can_slide(self, current_slide_length, max_slide_length):
    return max_slide_length is None or current_slide_length <= max_slide_length

  def __str__(self):
    return self.get_name().value
