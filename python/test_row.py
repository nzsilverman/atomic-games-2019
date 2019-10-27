import unittest
import client
import sys
    
class TestRow(unittest.TestCase):
  """ Tests to ensure the correct converetd token count when flipping tokens
      up and down. """
  def test_no_options(self):
    board = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],]
    returned_val = client.row_converted_tokens(1, board, [1, 1])
    expected_val = 0
    self.assertEqual(returned_val, expected_val)

  def test_full_row(self):
    board = [[0, 2, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0],
             [0, 2, 0, 0, 0, 0, 0, 0],]
    returned_val = client.row_converted_tokens(2, board, [0, 1])
    expected_val = 6
    self.assertEqual(returned_val, expected_val)

    returned_val = client.row_converted_tokens(2, board, [7, 1])
    expected_val = 6
    self.assertEqual(returned_val, expected_val)

  def test_partial_row(self):
    board = [[0, 2, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0],
             [0, 2, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0],
             [0, 2, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],]

    returned_val = client.row_converted_tokens(2, board, [0, 1])
    expected_val = 1
    self.assertEqual(returned_val, expected_val)

    returned_val = client.row_converted_tokens(2, board, [2, 1])
    expected_val = 1
    self.assertEqual(returned_val, expected_val)

    returned_val = client.row_converted_tokens(1, board, [4, 1])
    expected_val = 1
    self.assertEqual(returned_val, expected_val)

    returned_val = client.row_converted_tokens(1, board, [6, 1])
    expected_val = 1
    self.assertEqual(returned_val, expected_val)

  def test_ends_in_0(self):
    board = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0],
             [0, 2, 0, 0, 0, 0, 0, 0],
             [0, 2, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],]

    returned_val = client.row_converted_tokens(1, board, [1, 1])
    expected_val = 0
    self.assertEqual(returned_val, expected_val)

if __name__ == '__main__':
  unittest.main()