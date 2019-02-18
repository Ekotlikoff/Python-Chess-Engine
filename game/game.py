from model.color import Color
from model.board import Board
import random
import time
import threading

DEFAULT_TIME_PER_PLAYER = 60 * 20

class Game:
  def __init__(self, player_one, player_two, time_per_player=DEFAULT_TIME_PER_PLAYER):
    self.player_lock = threading.Lock()
    self.board = Board()
    self.game_over = False
    self.player_one = player_one
    self.time_elapsed_player_one = 0
    self.player_two = player_two
    self.time_elapsed_player_two = 0
    self.time_per_player = time_per_player
    self.total_ply = 0
    if random.randint(0, 1) is 0:
      self.player_one.set_color(Color.WHITE)
      self.player_two.set_color(Color.BLACK)
      self.current_turn = self.player_one
    else:
      self.player_one.set_color(Color.BLACK)
      self.player_two.set_color(Color.WHITE)
      self.current_turn = self.player_two
    self.player_one.set_game(self)
    self.player_two.set_game(self)
    self.player_one.set_lock(self.player_lock)
    self.player_two.set_lock(self.player_lock)
    self.game_running = False

  def get_current_turn(self):
    return self.current_turn

  def get_board(self):
    return self.board

  def is_game_over(self):
    return self.game_over

  def is_game_running(self):
    return self.game_running

  def get_time_elapsed(self, player):
    return self.time_elapsed_player_one if player is self.player_one else self.time_elapsed_player_two

  def switch_current_turn(self):
    if self.current_turn is self.player_one:
      self.current_turn = self.player_two
    else:
      self.current_turn = self.player_one

  def make_move(self, player, move):
    if not self.game_running:
      return
    if player is self.current_turn:
      if self.board.handle_move(move):
        time_elapsed = time.process_time() - self.turn_start
        if self.current_turn is self.player_one:
          self.time_elapsed_player_one += time_elapsed
        else:
          self.time_elapsed_player_two += time_elapsed
        self.switch_current_turn()
        self.turn_start = time.process_time()
        print('Time elapsed for player: ' + self.player_one.get_name() + ', ' + str(self.time_elapsed_player_one))
        print('Time elapsed for player: ' + self.player_two.get_name() + ', ' + str(self.time_elapsed_player_two))
        print(self.board)

  def run(self):
    print(self.board)
    self.turn_start = time.process_time()
    self.game_running = True
    while not self.game_over:
      time.sleep(.05)
      if self.current_turn is self.player_one:
        if self.time_elapsed_player_one > self.time_per_player:
          self.game_over = True
          self.winner = self.player_two
        elif self.board.is_checkmated(self.player_one.get_color()):
          print('Checkmate!')
          self.game_over = True
          self.winner = self.player_two
      else:
        if self.time_elapsed_player_two > self.time_per_player:
          self.game_over = True
          self.winner = self.player_one
        elif self.board.is_checkmated(self.player_two.get_color()):
          print('Checkmate!')
          self.game_over = True
          self.winner = self.player_one
    self.game_running = False
    print('WINNER IS ' + self.winner.name)
