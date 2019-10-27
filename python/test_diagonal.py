import unittest
import client
import sys
    
class TestDiagonal(unittest.TestCase):
  def test_diagonal_no_options(self):
    """ Test if can find all possible adjacent spaces """
    board = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],]
    returned_val = client.diagonal_converted_tokens(1, board, [1, 1], False)
    expected_val = 0
    self.assertEqual(returned_val, expected_val)

  def test_diagonal_up_right(self):
    """ Test if can find 1 spot up right. """
    board = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 2, 0, 0, 0, 0],
             [0, 0, 1, 2, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],]
    returned_val = client.diagonal_converted_tokens(1, board, [3, 2], False)
    expected_val = 1
    self.assertEqual(returned_val, expected_val)

  def test_diagonal_down_left(self):
    """ Test if can find 1 spot down left. """
    board = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 2, 0, 0, 0, 0],
             [0, 0, 1, 2, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],]
    returned_val = client.diagonal_converted_tokens(1, board, [1, 4], False)
    expected_val = 1
    self.assertEqual(returned_val, expected_val)

  def test_diagonal_up_left(self):
    """ Test if can find 1 spot up left. """
    board = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 2, 0, 0, 0, 0],
             [0, 0, 0, 2, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],]
    returned_val = client.diagonal_converted_tokens(1, board, [3, 4], False)
    expected_val = 1
    self.assertEqual(returned_val, expected_val)

  def test_diagonal_down_right(self):
    """ Test if can find 1 spot down right. """
    board = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 2, 0, 0, 0, 0],
             [0, 0, 0, 2, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],]
    returned_val = client.diagonal_converted_tokens(1, board, [1, 2], False)
    expected_val = 1
    self.assertEqual(returned_val, expected_val)

  def test_diagonal_all_directions(self):
    """ Test if can find sum of diagonals in all directions. """
    board = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 1, 0],
             [0, 0, 0, 2, 0, 2, 0, 0],
             [0, 0, 0, 2, 1, 0, 0, 0],
             [0, 0, 0, 2, 0, 2, 0, 0],
             [0, 0, 1, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],]
    returned_val = client.diagonal_converted_tokens(1, board, [3, 4], False)
    expected_val = 4
    self.assertEqual(returned_val, expected_val)

  def test_diagonal_none_top_row(self):
    board = [[0, 0, 2, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],]
    returned_val = client.diagonal_converted_tokens(1, board, [1, 1], False)
    expected_val = 0
    self.assertEqual(returned_val, expected_val)

  def test_diagonal_none_col_zero(self):
    board =  [[0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 0, 0, 0],
              [2, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],]
    returned_val = client.diagonal_converted_tokens(1, board, [1, 1], False)
    expected_val = 0
    self.assertEqual(returned_val, expected_val)
  
  def test_diagonal_none_last_row(self):
    board =  [[0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 2],]
    returned_val = client.diagonal_converted_tokens(1, board, [6, 6], False)
    expected_val = 0
    self.assertEqual(returned_val, expected_val)

  def test_diagonal_none_last_col(self):
    board =  [[0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 2],
              [0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],]
    returned_val = client.diagonal_converted_tokens(1, board, [6, 6], False)
    expected_val = 0
    self.assertEqual(returned_val, expected_val)

  def test_diagonal_ending_on_edge_non_player(self):
    board =  [[0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 2, 0],
              [0, 0, 0, 0, 0, 0, 0, 2],]
    returned_val = client.diagonal_converted_tokens(1, board, [5, 5], False)
    expected_val = 0
    self.assertEqual(returned_val, expected_val)

  def test_diagonal_ending_on_edge_player(self):
    board =  [[1, 0, 0, 0, 1, 0, 0, 0],
              [0, 2, 0, 2, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 2, 0],
              [0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 2, 0],
              [0, 0, 0, 0, 0, 0, 0, 1],]
    returned_val = client.diagonal_converted_tokens(1, board, [2, 2], False)
    expected_val = 2
    self.assertEqual(returned_val, expected_val)
    returned_val = client.diagonal_converted_tokens(1, board, [5, 5], False)
    expected_val = 2
    self.assertEqual(returned_val, expected_val)

  def test_diagonal_starting_on_edge(self):
    board =  [[0, 0, 1, 0, 0, 0, 0, 0],
              [0, 2, 0, 0, 0, 0, 0, 0],
              [1, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 2, 0],
              [0, 0, 0, 0, 0, 1, 0, 0],]
    returned_val = client.diagonal_converted_tokens(1, board, [0, 2], False)
    expected_val = 1
    self.assertEqual(returned_val, expected_val)

    returned_val = client.diagonal_converted_tokens(1, board, [2, 0], False)
    expected_val = 1
    self.assertEqual(returned_val, expected_val)

    returned_val = client.diagonal_converted_tokens(1, board, [5, 7], False)
    expected_val = 1
    self.assertEqual(returned_val, expected_val)

    returned_val = client.diagonal_converted_tokens(1, board, [7, 5], False)
    expected_val = 1
    self.assertEqual(returned_val, expected_val)

  def test_long_diagonal(self):
    board =  [[1, 0, 0, 0, 0, 0, 0, 1],
              [0, 2, 0, 0, 0, 0, 2, 0],
              [0, 0, 2, 0, 0, 2, 0, 0],
              [0, 0, 0, 2, 2, 0, 0, 0],
              [0, 0, 0, 2, 2, 0, 0, 0],
              [0, 0, 2, 0, 0, 2, 0, 0],
              [0, 2, 0, 0, 0, 0, 2, 0],
              [1, 0, 0, 0, 0, 0, 0, 1],]
    returned_val = client.diagonal_converted_tokens(1, board, [0, 0], False)
    expected_val = 6
    self.assertEqual(returned_val, expected_val)

    returned_val = client.diagonal_converted_tokens(1, board, [0, 7], False)
    expected_val = 6
    self.assertEqual(returned_val, expected_val)

    returned_val = client.diagonal_converted_tokens(1, board, [7, 0], False)
    expected_val = 6
    self.assertEqual(returned_val, expected_val)

    returned_val = client.diagonal_converted_tokens(1, board, [7, 7], False)
    expected_val = 6
    self.assertEqual(returned_val, expected_val)

if __name__ == '__main__':
  unittest.main()