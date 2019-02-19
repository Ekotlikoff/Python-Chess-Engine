from tkinter import Tk, Frame, Label
import threading
import time
from model.board import BOARD_DIMENSION
from model.pieces.constants import Pieces
from model.color import Color
import queue

WIDTH = 600
HEIGHT = 600

class View:
  def __init__(self, game, master=Tk()):
    self.master = master
    self.game = game
    self.board = self.game.get_board_safely()
    self.labels = []
    self.draw_grid()

  def draw_grid(self):
    for label in self.labels:
      label.destroy()
    for rank_index in range(BOARD_DIMENSION):
      for file_index in range(BOARD_DIMENSION):
        piece = self.board.get((file_index, rank_index))
        color = 'snow'
        if piece is not None and piece.get_color() is Color.WHITE:
          color = 'linen'
        elif piece is not None:
          color = 'grey55'
        row = rank_index
        rect = Label(self.master, text=str(piece), bg=color, borderwidth=1)
        self.labels.append(rect)
        rect.grid(column=file_index, row=row, sticky='')
        self.master.grid_columnconfigure(file_index, weight=1)
        self.master.grid_rowconfigure(row, weight=1)
 
  def set_board(self, board):
    self.board = board
    self.draw_grid()
    self.master.update()

  def run(self):
    self.master.mainloop()
