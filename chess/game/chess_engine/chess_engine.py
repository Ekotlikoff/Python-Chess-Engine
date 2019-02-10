import time
import random
import threading

class ChessEngine():
  def __init__(self, name):
    self.name = name
    self.color = None
    self.thread = threading.Thread(target=self.run)

  def set_game(self, game):
    self.game = game

  def get_name(self):
    return self.name

  def start(self):
    self.thread.start()

  def run(self):
    while not self.game.is_game_over():
      if self.game.is_game_running() and self.game.get_current_turn() is self:
        self.choose_move(self.game)
      else:
        time.sleep(1)

  def set_color(self, color):
    self.color = color

  def choose_move(self, game):
    if self.color is None:
      print("Invalid state, player must know their color")
      raise ValueError("Player must know their color")
    my_pieces = game.get_board().get_pieces(self.color)
    valid_moves = []
    for piece in my_pieces:
      valid_moves += piece.get_valid_moves()
    next_move = random.choice(valid_moves)
    print(next_move)
    game.make_move(self, next_move)
