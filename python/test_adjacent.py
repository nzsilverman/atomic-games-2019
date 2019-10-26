import unittest
import client
import sys

class TestAdjacentMoves(unittest.TestCase):
  """ These tests are designed to stress the implementation of the adjacent_moves
      function. The adjacent_moves function returns a list of items, which in 
      some cases is hard to evaluate by checking if it is equal to another list
      because the return list is dependent upon the algorithm implementation. This is
      a fault in these test cases, and can be improved upon later. However, they are
      functionally correct and do test the program. """

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

  def test_no_duplicates_returned(self):
    """ Test if can find all possible adjacent spaces """
    board = [[0, 1, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],]
    returned_list = client.adjacent_moves(2, board)
    expected_list = [[0, 0], 
                     [1, 0],
                     [1, 1], 
                     [1, 2], 
                     [0, 3],
                     [1, 3]] 
    self.assertEqual(returned_list, expected_list)
    

if __name__ == '__main__':
  unittest.main()