from model.color import Color
from model.board import Board
from model.move import Move
from model.pieces.constants import Pieces
import pytest

@pytest.fixture()
def board():
  yield Board()

class TestBoard:
  def test_valid_moves_pawn(self, board):
    assert len(board.get((0,1)).get_valid_moves()) == 2

  def test_valid_moves_of_promoted_pawn(self, board):
    board.handle_move(Move(board.get((0,1)), (0,3), False))
    assert board is board.get((0,3)).get_board()
    board.handle_move(Move(board.get((0,3)), (0,4), False))
    board.handle_move(Move(board.get((0,4)), (0,5), False))
    board.handle_move(Move(board.get((0,5)), (1,6), True))
    assert len([move for move in board.get((1,6)).get_valid_moves() if move.get_promoting_to() is not None]) == 4
    promote_to_queen_move = next((move for move in board.get((1,6)).get_valid_moves() if move.get_new_position() == (0, 7) and move.get_promoting_to().get_name() == Pieces.QUEEN))
    board.handle_move(promote_to_queen_move)
    assert board is board.get((0,7)).get_board()
    assert len(board.get((0,7)).get_valid_moves()) == 7
