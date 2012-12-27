import unittest

from solver import is_valid

class IsValidTestCase(unittest.TestCase):
    def setUp(self):
        self.valid = [5, 3, 6, 0, 7, 1, 4, 2]
        self.invalid_row = [5, 5]
        self.invalid_diag = [0, 1]

    def test_same_col(self):
        self.assertFalse(is_valid(self.invalid_row))

    def test_same_diag(self):
        self.assertFalse(is_valid(self.invalid_diag))

    def test_valid(self):
        self.assertTrue(is_valid(self.valid))
#class IsValidTupleTestCase(unittest.TestCase):
    #def setUp(self):
        #self.valid_tuple = ((6,-1), (5,1), (4,-2), (3,4), (2,-3), (1,3), (0,0), (-1,2))
        #self.invalid_tuple = ((6,0), (5,1), (4,-2), (3,4), (2,-3), (1,3), (0,0), (-1,2))
        #self.invalid_diag = ((6,-1), (6,6), (4,-2), (3,4), (2,-3), (1,3), (0,0), (-1,2))
        #self.invalid_row = ((6,-1), (0,7), (4,-2), (3,4), (2,-3), (1,3), (0,0), (-1,2))
        #self.invalid_col = ((6,-1), (7,0), (4,-2), (3,4), (2,-3), (1,3), (0,0), (-1,2))

    #def test_valid_tuple(self):
        #self.assertTrue(is_valid(self.valid_tuple))

    #def test_invalid_tuple(self):
        #self.assertFalse(is_valid(self.invalid_tuple))

    #def test_invalid_diag(self):
        #self.assertFalse(is_valid(self.invalid_diag))

    #def test_invalid_row(self):
        #self.assertFalse(is_valid(self.invalid_row))

    #def test_invalid_col(self):
        #self.assertFalse(is_valid(self.invalid_col))

#class IsSafeTestCase(unittest.TestCase):
    #def setUp(self):
        #self.board = range(SIZE * SIZE)

    #def test_no_queens(self):
        #self.assertTrue(is_safe(self.board, 0))
        #self.assertTrue(is_safe(self.board, 3))
        #self.assertTrue(is_safe(self.board, 63))

    #def test_same_col_failure(self):
        #self.board[0] = 'Q'
        #self.assertFalse(is_safe(self.board, 8))
        #self.assertFalse(is_safe(self.board, 16))
        #self.assertFalse(is_safe(self.board, 24))
        #self.assertFalse(is_safe(self.board, 32))
        #self.assertFalse(is_safe(self.board, 40))
        #self.assertFalse(is_safe(self.board, 48))
        #self.assertFalse(is_safe(self.board, 56))
        #self.assertFalse(is_safe(self.board, 0))

    #def test_same_row_failure(self):
        #self.board[15] = 'Q'
        #self.assertFalse(is_safe(self.board, 14))
        #self.assertFalse(is_safe(self.board, 13))
        #self.assertFalse(is_safe(self.board, 12))
        #self.assertFalse(is_safe(self.board, 11))
        #self.assertFalse(is_safe(self.board, 10))
        #self.assertFalse(is_safe(self.board, 9))
        #self.assertFalse(is_safe(self.board, 8))

    #def test_diagonal_failure(self):
        #self.board[9] = 'Q'
        #self.assertFalse(is_safe(self.board, 0))
        #self.assertFalse(is_safe(self.board, 9))
        #self.assertFalse(is_safe(self.board, 18))
        #self.assertFalse(is_safe(self.board, 27))
        #self.assertFalse(is_safe(self.board, 36))
        #self.assertFalse(is_safe(self.board, 45))
        #self.assertFalse(is_safe(self.board, 54))
        #self.assertFalse(is_safe(self.board, 63))

    #def test_one_queen(self):
        #self.board[0] = 'Q'
        #self.assertTrue(is_safe(self.board, 11))
        #self.assertTrue(is_safe(self.board, 12))
        #self.assertFalse(is_safe(self.board, 4))
        #self.assertFalse(is_safe(self.board, 1))
        #self.assertFalse(is_safe(self.board, 9))
        #self.assertFalse(is_safe(self.board, 0))



if __name__ == '__main__':
    unittest.main()
