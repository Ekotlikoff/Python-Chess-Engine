class Move:
  def __init__(self, piece, new_position, is_capture, capturing_position=None, castling_with=None, promoting_to=None):
    self.piece = piece
    self.new_position = new_position
    self.castling_with = castling_with
    self.is_capture = is_capture
    self.capturing_position = capturing_position
    self.promoting_to = promoting_to
    self.original_position = piece.get_position()

  def get_original_position(self):
    return self.original_position

  def get_new_position(self):
    return self.new_position

  def get_piece(self):
    return self.piece

  def get_capturing_position(self):
    return self.capturing_position

  def get_castling_with(self):
    return self.castling_with

  def get_promoting_to(self):
    return self.promoting_to

  def set_promoting_to(self, promoting_to):
    self.promoting_to = promoting_to

  def __str__(self):
    return str(self.piece) + ' ' + str(self.new_position) + ' is_capture: ' + str(self.is_capture)

  def __repr__(self):
    return 'Move(' + str(self.piece) + ', ' + str(self.piece.get_position()) + ', ' + str(self.new_position) + ', ' + str(self.is_capture) + ')'
