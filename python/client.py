#!/usr/bin/python

# Develop branch
# This branch is an attempt at a miniMax implementation. In the repo
# there are documents that describe how to implement miniMax. This 
# code is an attempt at implementing that. It does not work yet. It does
# not error out, but it is not as succesful as it should be. The issues 
# are related to storing the best state throughout the life cycle of calling
# miniMax recursively. This code could probably be adapted to work 
# succesfully but it does not yet

import sys
import json
import socket
from enum import Enum
import copy

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
  # board = list(board_in)
  board = copy.deepcopy(board_in)

  for row in range(0, BOARD_WIDTH):
    for col in range(0, BOARD_HEIGHT):
      if board[row][col] == 1 or board[row][col] == 2:
        # Found a spot that there could potentially be adjacent moves from
        if board[row][col] != player:
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
      
# player = 1 or 2
# board = board passsed in
# val = num tiles could flip 
# pos = position in format [x, x]
# row_pos = row positive, should row go to the right (+) or left (-)
# col_pos = col positive, should col go up (+) or down (-)
# dir_type = which direction to search? diagonal, column, row
# flip_tokens = should flip tokens along search? ONLY CALL IF KNOWN TO END IN TOKEN_COUNT > 0
# or if a copy of the board was passed in
def count_helper(player, board, pos, val, row_pos, col_pos, dir_type, flip_tokens):
  row = pos[0]
  col = pos[1]
  if (row < 0 or row >= BOARD_HEIGHT or col < 0 or col >= BOARD_HEIGHT):
    # Out of bounds, return 0
    return 0
  elif board[row][col] == 0:
    # Reached as far as they can go
    # Square is a zero, so cannot flip the tiles
    return 0
  elif (board[row][col] == player):
    # Reached as far as they can go, can flip the tiles
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
    # flip token if we are told to do so.
    # This will only be called when we know we will reach a succesful end
    if flip_tokens:
      board[row][col] = player
    # Recurse
    return count_helper(player, board, new_pos, val+1, row_pos, col_pos, dir_type, flip_tokens) 

def diagonal_converted_tokens(player, board, pos, flip_tokens):
  """ Evaluates and returns how many tokens will be converted when a player occupied
      the position passed in. Evaluates for all four diagonal directions. """
  row = pos[0]
  col = pos[1]
  # Need to evaluate how many tokens will be gained in each direction from a 
  # specific move
  up_right =    count_helper(player, board, [row-1, col+1], 0, False, True, Dir.DIAGONAL, flip_tokens)
  down_right =  count_helper(player, board, [row+1, col+1], 0, True, True, Dir.DIAGONAL, flip_tokens)
  up_left =     count_helper(player, board, [row-1, col-1], 0, False, False, Dir.DIAGONAL, flip_tokens)
  down_left =   count_helper(player, board, [row+1, col-1], 0, True, False, Dir.DIAGONAL, flip_tokens)
  return up_right + down_right + up_left + down_left

def column_converted_tokens(player, board, pos, flip_tokens):
  """ Evaluates and returns how many tokens will be converted when a player occupies 
      the position that is passed in. Evaluates up and down directions.
      It is called column_converted because the column value is changed. """
  row = pos[0]
  col = pos[1]
  left =  count_helper(player, board, [row, col-1], 0, False, False, Dir.COLUMN, flip_tokens)
  right = count_helper(player, board, [row, col+1], 0, False, True, Dir.COLUMN, flip_tokens)
  return left + right

def row_converted_tokens(player, board, pos, flip_tokens):
  """ Evaluates and returns how many tokens will be converted when a player occupies 
      the position that is passed in. Evaluates left and right directions. It
      is called row_converted because the row value is changed. """
  row = pos[0]
  col = pos[1]
  up =  count_helper(player, board, [row-1, col], 0, False, False, Dir.ROW, flip_tokens)
  down = count_helper(player, board, [row+1, col], 0, True, False, Dir.ROW, flip_tokens)
  return up + down

def get_valid_moves(player, board):
  """ Returns a list of tuples: [(valid_move, flipped_count, board_after), ...]. """
  all_moves = adjacent_moves(player, board)
  valid_moves = []
  for move in all_moves:
    # Copy the board so that we can update it as we search
    board_copy = copy.deepcopy(board)
    count = 0
    count += diagonal_converted_tokens(player, board_copy, move, True)
    count += row_converted_tokens(player, board_copy, move, True)
    count += column_converted_tokens(player, board_copy, move, True)

    if count > 0:
      # Found a valid move
      valid_moves.append((move, count, board_copy))
  
  return valid_moves

# Determine if it is a terminal node, i.e. cannot move further
def isTerminalNode(player, board):
  valid_moves = get_valid_moves(player, board)
  if valid_moves:
    return False
  return True

def EvalBoard(player, board):
  """ Evaulate the final board state, and assign point values based on differnt board positions. """
  score = 0
  for row in range(0, BOARD_HEIGHT):
    for col in range(0, BOARD_WIDTH):
      if board[row][col] == player:
        if (col == 0 or col == BOARD_WIDTH-1) and (row == 0 or row == BOARD_HEIGHT-1):
          # corner square
          score += 4 # Value of corner 
        elif (col == 0 or col == BOARD_WIDTH-1) or (row == 0 or row == BOARD_HEIGHT-1):
          # side square
          score += 2 # Side valuation 
        else:
          score += 1

  return score

def miniMaxAttempt2(player, board, depth, maximizingPlayer):
  """ Attempt at implementing miniMax. This version was based on the whitepapers in the repo mainly. """
  if depth == 0 or isTerminalNode(player, board):
    return EvalBoard(player, board)
  if maximizingPlayer:
    best = 0 # start lowest possible
    valid_moves = get_valid_moves(player, board)
    for move in valid_moves:
      tmp_player = 1 if player == 2 else 2
      val = int(miniMaxAttempt2(tmp_player, move[2], depth - 1, False))
      best = max(best, val)
  else: 
    # minimizing player
    best = sys.maxsize # start highest possible
    valid_moves = get_valid_moves(player, board)
    for move in valid_moves:
      tmp_player = 1 if player == 2 else 2
      val = int(miniMaxAttempt2(tmp_player, move[2], depth - 1, True))
      best = min(best, val)
  return best

def get_move(player, board):
  """ Return the best move to play. """
  try:
    # min_max = minMax(player, board, False, [], 0)
    # min_max = minMaxIterative(player, board, True)

    # Idea, get all valid moves, and then iterate through them and call miniMax 
    # to try and find the one that returns the highest score. I think this is the root issue
    # with this minimax implementation. I think it needs to be called on the current player with 
    # True passed in
    valid_moves = get_valid_moves(player, board)
    best = 0
    depth = 3
    best_move = []
    for move in valid_moves:
      tmp_player = 1 if player == 2 else 1
      # Since we are calling this on each from the top level search
      # pass in false and the opposite player
      score = int(miniMaxAttempt2(tmp_player, move[2], depth, False))
      if score >= best:
        best = score 
        best_move = move[0]

  except Exception as e:
    # If miniMax is broken, instead of breaking use get_valid_moves and return the first, which 
    # is just a random choice. It is not optimal, but prevents failure
    print("error getting min Max: {}".format(e))
    valid_moves = get_valid_moves(player, board)
    return valid_moves[0][0]
  print("Best score: {}".format(best))
  return best_move

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

      try:
        move = get_move(player, board)
      except:
        print("Error getting move, exiting")
        exit(0)
      try:
        response = prepare_response(move)
      except:
        print("Error preparing response, exiting")
        exit(0)
      sock.sendall(response)
  finally:
    sock.close()
