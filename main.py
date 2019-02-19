from model.board import Board
from game.game import Game
from game.chess_engine.chess_engine import ChessEngine
from game.human_player import HumanPlayer

player_one = ChessEngine('Engine 1')
name = input('Enter your name: ')
player_two = HumanPlayer(name)
RUN_AS_GUI = False

game = Game(player_one, player_two, RUN_AS_GUI)

player_one.start()
player_two.start()
game.start()

if RUN_AS_GUI:
  from game.view import View
  
  view = View(game)
  game.register_view(view)
  view.run()
