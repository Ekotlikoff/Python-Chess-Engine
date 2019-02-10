from model.board import Board
from game.game import Game
from game.chess_engine.chess_engine import ChessEngine
from game.human_player import HumanPlayer

player_one = ChessEngine('Engine 1')
player_two = HumanPlayer(input('Enter your name: '))

game = Game(player_one, player_two)

player_one.start()
player_two.start()
game.run()
