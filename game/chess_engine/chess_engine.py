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

  def set_lock(self, lock):
    self.lock = lock

  def start(self):
    self.thread.start()

  def run(self):
    while True:
      with self.lock:
        if self.game.is_game_running() and self.game.get_current_turn() is self:
          self.choose_move(self.game)
        elif self.game.is_game_over():
          return
        else:
          time.sleep(1)
          

  def set_color(self, color):
    self.color = color

  def get_color(self):
    return self.color

  def choose_move(self, game):
    if self.color is None:
      print("Invalid state, player must know their color")
      raise ValueError("Player must know their color")
    valid_moves = game.get_board().get_all_valid_moves(self.color)
    next_move = random.choice(valid_moves)
    game.make_move(self, next_move)
