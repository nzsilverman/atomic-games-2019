import unittest
import client
import sys
    
class TestColumn(unittest.TestCase):
  """ Tests to ensure the correct converetd token count when flipping tokens
      to the left and right. """
  def test_no_options(self):
    board = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],]
    returned_val = client.column_converted_tokens(1, board, [1, 1])
    expected_val = 0
    self.assertEqual(returned_val, expected_val)

  def test_entire_row(self):
    board = [[0, 0, 0, 0, 0, 0, 0, 0],
             [1, 2, 2, 2, 2, 2, 2, 1],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],]
    returned_val = client.column_converted_tokens(1, board, [1, 0])
    expected_val = 6
    self.assertEqual(returned_val, expected_val)

    returned_val = client.column_converted_tokens(1, board, [1, 7])
    expected_val = 6
    self.assertEqual(returned_val, expected_val)

  def test_partial_row(self):
    board = [[0, 0, 0, 0, 0, 0, 0, 0],
             [1, 2, 1, 2, 2, 2, 2, 1],
             [1, 1, 1, 2, 2, 2, 2, 1],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],]
    returned_val = client.column_converted_tokens(1, board, [1, 0])
    expected_val = 1
    self.assertEqual(returned_val, expected_val)

    returned_val = client.column_converted_tokens(1, board, [2, 2])
    expected_val = 4
    self.assertEqual(returned_val, expected_val)

if __name__ == '__main__':
  unittest.main()