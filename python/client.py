#!/usr/bin/python

import sys
import json
import socket
from enum import Enum

BOARD_WIDTH = 8
BOARD_HEIGHT = 8

def print_board(board):
  for row in board:
    print(row)
    
def adjacent_moves(player, board_in):
  """ Returns a list of lists of adjacent moves that the player passed in could make. """
  adj_moves = []

  # Create a copy of the board_in so that we can mark spots that were 
  # added, but not change the original. We only want to add to the adj_moves
  # once, and adding a tuple (i.e. [2, 3]) does not play well with a set 
  # so this is a way around using a set data structure, and keeping the moves
  # in an easy to work with format
  board = board_in

  for row in range(0, BOARD_WIDTH):
    for col in range(0, BOARD_HEIGHT):
      if board[row][col] == 1 or board[row][col] == 2:
        # Found a spot that there could potentially be adjacent moves from
        if board[row][col] is not player:
          # Iterate over elements in the square [row-1, row+1] and [col-1, col+1]
          # The bounds are row+2 and col+2 because the range is not inclusive
          # An element within this range is valid as long as it is in bounds, and
          # is not yet occupied
          for tmp_row in range(row-1, row+2):
            for tmp_col in range(col-1, col+2):
              if (tmp_row >= 0 and tmp_col >= 0 and
                  tmp_row < BOARD_HEIGHT and tmp_col < BOARD_WIDTH):
                # In bounds
                if board[tmp_row][tmp_col] == 0:
                  # Square is free, can add to adjacent moves set 
                  adj_moves.append([tmp_row, tmp_col])
                  board[tmp_row][tmp_col] = "F"

  return adj_moves

class Dir(Enum):
  DIAGONAL = 1
  COLUMN = 2
  ROW = 3
      
def count_helper(player, board, pos, val, row_pos, col_pos, dir_type):
  row = pos[0]
  col = pos[1]
  if (row < 0 or row >= BOARD_HEIGHT or col < 0 or col >= BOARD_HEIGHT):
    # Out of bounds, return 0
    return 0
  elif ((row == 0 or col == 0 or row == BOARD_HEIGHT-1 or col == BOARD_WIDTH-1)
     and board[row][col] == player):
    # Edge spot on the board, and player can flip the tiles 
    # They reached in getting to this spot
    return val 
  elif (row == 0 or col == 0 or row == BOARD_HEIGHT-1 or col == BOARD_WIDTH-1):
    # Edge spot on the board, player cannot flip the tiles
    # they reached to get her because the last tile is not theirs
    return 0
  elif (board[row][col] == 0 or board[row][col] == player):
    # Reached as far as they can go, still not the edge of the board
    return val 
  elif board[row][col] != player:
    # Need to keep recursing, since token in spot is not the player 
    
    # Figure out next spot to recurse to based on bool flags passed in
    if dir_type == Dir.DIAGONAL:
      # Diagonal recursion, adjust both column and row
      new_row = row+1 if row_pos else row-1
      new_col = col+1 if col_pos else col-1
      new_pos = [new_row, new_col]
    elif dir_type == Dir.COLUMN:
      new_col = col+1 if col_pos else col-1
      new_pos = [row, new_col]
    elif dir_type == Dir.ROW:
      new_row = row+1 if row_pos else row-1
      new_pos = [new_row, col]


    # Recurse
    return count_helper(player, board, new_pos, val+1, row_pos, col_pos, dir_type) 

def diagonal_converted_tokens(player, board, pos):
  """ Evaluates and returns how many tokens will be converted when a player occupied
      the position passed in. Evaluates for all four diagonal directions. """
  row = pos[0]
  col = pos[1]
  # Need to evaluate how many tokens will be gained in each direction from a 
  # specific move
  up_right =    count_helper(player, board, [row-1, col+1], 0, False, True, Dir.DIAGONAL)
  down_right =  count_helper(player, board, [row+1, col+1], 0, True, True, Dir.DIAGONAL)
  up_left =     count_helper(player, board, [row-1, col-1], 0, False, False, Dir.DIAGONAL)
  down_left =   count_helper(player, board, [row+1, col-1], 0, True, False, Dir.DIAGONAL)
  return up_right + down_right + up_left + down_left

def column_converted_tokens(player, board, pos):
  """ Evaluates and returns how many tokens will be converted when a player occupies 
      the position that is passed in. Evaluates left and right directions. """
  row = pos[0]
  col = pos[1]
  left =  count_helper(player, board, [row, col-1], 0, False, False, Dir.COLUMN)
  right = count_helper(player, board, [row, col+1], 0, False, True, Dir.COLUMN)
  return left + right

def row_converted_tokens(player, board, pos):
  """ Evaluates and returns how many tokens will be converted when a player occupies 
      the position that is passed in. Evaluates up and down directions. """
  row = pos[0]
  col = pos[1]
  up =  count_helper(player, board, [row-1, col], 0, False, False, Dir.ROW)
  down = count_helper(player, board, [row+1, col], 0, True, False, Dir.ROW)
  return up + down

def get_move(player, board):
  # TODO determine valid moves
  # TODO determine best move
  return [2, 3]

def prepare_response(move):
  response = '{}\n'.format(move).encode()
  print('sending {!r}'.format(response))
  return response

if __name__ == "__main__":
  port = int(sys.argv[1]) if (len(sys.argv) > 1 and sys.argv[1]) else 1337
  host = sys.argv[2] if (len(sys.argv) > 2 and sys.argv[2]) else socket.gethostname()

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    sock.connect((host, port))
    while True:
      data = sock.recv(1024)
      if not data:
        print('connection to server closed')
        break
      json_data = json.loads(str(data.decode('UTF-8')))
      board = json_data['board']
      maxTurnTime = json_data['maxTurnTime']
      player = json_data['player']
      print(player, maxTurnTime, board)

      move = get_move(player, board)
      response = prepare_response(move)
      sock.sendall(response)
  finally:
    sock.close()
