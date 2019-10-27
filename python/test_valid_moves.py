import unittest
import client
import sys
    
class TestValidMoves(unittest.TestCase):
  def test_multiple_options(self):
    """ This test was input that broke the program before. """
    board =  [[0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 2, 0, 0, 0],
              [0, 0, 0, 0, 2, 0, 0, 0],
              [0, 0, 0, 2, 2, 0, 0, 0],
              [0, 0, 2, 2, 2, 2, 0, 0],
              [0, 0, 1, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0]]

    valid_moves = client.get_valid_moves(1, board)
    expected_val = [[3, 2],
                    [3, 5],
                    [2, 5],
                    [2, 2]]
    self.assertEqual(len(expected_val), len(valid_moves))

  def test_no_options_left(self):
    """ This test broke the program when testing against the ai. """
    board =  [[2, 2, 2, 2, 2, 1, 1, 1],
              [2, 1, 2, 2, 2, 1, 1, 2],
              [2, 2, 1, 2, 1, 1, 1, 1],
              [2, 2, 2, 1, 1, 2, 1, 1],
              [2, 1, 2, 2, 1, 2, 1, 2],
              [2, 1, 1, 1, 2, 1, 1, 2],
              [2, 1, 1, 1, 1, 2, 1, 2],
              [2, 1, 2, 0, 1, 2, 2, 0]]
    diag_count = client.diagonal_converted_tokens(1, board, [7,3], False)
    self.assertEqual(diag_count, 0)
    # import pdb; pdb.set_trace()
    col_count = client.column_converted_tokens(1, board, [7,3], False)
    self.assertEqual(col_count, 1)
    row_count = client.row_converted_tokens(1, board, [7,3], False)
    self.assertEqual(row_count, 0)
    valid_moves = client.get_valid_moves(1, board)
    expected_val = [[7, 3],
                    [7, 7]]
    client.print_board(board)
    print("Valid Moves Returned: ")
    print(valid_moves)
    print("\nExpected Valid Moves: ")
    print(expected_val)
    self.assertEqual(len(expected_val), len(valid_moves))
  

if __name__ == '__main__':
  unittest.main()