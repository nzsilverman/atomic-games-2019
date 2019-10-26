import unittest
import client
import logging
import sys

# class TestGetMove(unittest.TestCase):
#   def test_get_move_returns_a_valid_move(self):
#     board = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 2, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
#     self.assertEqual(client.get_move(1, board), [2, 3])
# 
# class TestPrepareResponse(unittest.TestCase):
#   def test_prepare_response_returns_a_valid_response(self):
#     self.assertEqual(client.prepare_response([2, 3]), b'[2, 3]\n')

class TestAdjacentMoves(unittest.TestCase):
  def test_returns_adjacent_moves_set_basic(self):
    """ Test if can find all possible adjacent spaces """
    board = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],]
    returned_list = client.adjacent_moves(2, board)
    expected_list = [[0,0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]]
    self.assertEqual(returned_list, expected_list)

  def test_returns_adjacent_move_only_one_adjacent(self):
    """ Test if can find the one possible adjacent space. """
    board = [[2, 2, 2, 0, 0, 0, 0, 0],
             [0, 1, 2, 0, 0, 0, 0, 0],
             [2, 2, 2, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],]
    returned_list = client.adjacent_moves(2, board)
    expected_list = [[1, 0]]
    self.assertEqual(returned_list, expected_list)

  def test_adjacent_no_adjacent(self):
    """ Test if can find the one possible adjacent space. """
    board = [[2, 2, 2, 0, 0, 0, 0, 0],
             [2, 1, 2, 0, 0, 0, 0, 0],
             [2, 2, 2, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],]
    returned_list = client.adjacent_moves(2, board)
    self.assertEqual(len(returned_list), 0)

  def test_adjacent_edge_cases(self):
    """ Test if can find all possible adjacent spaces """
    board = [[0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 1],]
    returned_list = client.adjacent_moves(2, board)
    expected_list = [[0, 0], 
                     [0, 2], 
                     [1, 0],
                     [1, 1],
                     [1, 2],
                     [6, 0],
                     [6, 1],
                     [6, 2],
                     [7, 0],
                     [7, 2],
                     [6, 6],
                     [6, 7],
                     [7, 6]]
    self.assertEqual(returned_list, expected_list)

if __name__ == '__main__':
  logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
  unittest.main()