import time
import random
import threading
from model.move import Move

class HumanPlayer():
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
    print('Welcome, ' + self.get_name() + ', your color is: ' + str(self.color))
    while not self.game.is_game_over():
      if self.game.is_game_running() and self.game.get_current_turn() is self:
        self.choose_move(self.game)
      else:
        time.sleep(.05)

  def set_color(self, color):
    self.color = color

  def get_color(self):
    return self.color

  def choose_move(self, game):
    if self.color is None:
      raise ValueError("Player must know their color")
    human_coordinates = input('Enter your move in coordinate notation, e.g. e2-e4: \n')
    move = self.human_coordinates_to_move(human_coordinates)
    my_pieces = game.get_board().get_pieces(self.color)
    valid_moves = []
    for piece in my_pieces:
      valid_moves += piece.get_valid_moves()
    valid_move = None if move is None else next((m for m in valid_moves if m.get_original_position() == move[0] and m.get_new_position() == move[1]), None)
    while valid_move is None:
      my_pieces = game.get_board().get_pieces(self.color)
      human_coordinates = input('Invalid move, enter your move in coordinate notation, e.g. e2-e4: ')
      move = self.human_coordinates_to_move(human_coordinates)
      valid_move = None if move is None else next((m for m in valid_moves if m.get_original_position() == move[0] and m.get_new_position() == move[1]), None)
    game.make_move(self, valid_move)

  def human_coordinates_to_move(self, human_coordinates):
    coordinates = human_coordinates.split('-')
    if len(coordinates) is not 2:
      return None
    try:
      from_coordinate = coordinates[0]
      to_coordinate = coordinates[1]
      from_file = ord(from_coordinate[0]) - 97
      from_rank = int(from_coordinate[1]) - 1
      from_position = (from_file, from_rank)
      to_file = ord(to_coordinate[0]) - 97
      to_rank = int(to_coordinate[1]) - 1
      to_position = (to_file, to_rank)
    except:
      return None
    return [from_position, to_position]
