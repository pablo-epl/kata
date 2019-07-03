import codewars_test as test

'''
Sudoku Background
Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all
cells of the grid with digits from 1 to 9, so that each column, each row,
and each of the nine 3x3 sub-grids (also known as blocks) contain all of
the digits from 1 to 9. (More info at: http://en.wikipedia.org/wiki/Sudoku)

Sudoku Solution Validator
Write a function validSolution/ValidateSolution/valid_solution() that accepts
a 2D array representing a Sudoku board, and returns true if it is a valid
solution, or false otherwise. The cells ofthe sudoku board may also contain
0's, which will represent empty cells. Boards containing one or more zeroes are
considered to be invalid solutions.

The board is always 9 cells by 9 cells, and every cell only contains
integers from 0 to 9.

Examples

```
validSolution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
]) // => true

validSolution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 0, 3, 4, 8],
  [1, 0, 0, 3, 4, 2, 5, 6, 0],
  [8, 5, 9, 7, 6, 1, 0, 2, 0],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 0, 1, 5, 3, 7, 2, 1, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 0, 0, 4, 8, 1, 1, 7, 9]
]) // => false
```

'''

def valid_solution(board):
    valid_board_solution = True
    board_columns = get_columns_as_rows(board)
    board_block_sets = get_block_sets_as_rows(board)
    for column_block_set in board_columns:
        if not validate_set(column_block_set):
            valid_board_solution = False
    for row_block_set in board:
        if not validate_set(row_block_set):
            valid_board_solution = False
    for block_set in board_block_sets:
        if not validate_set(block_set):
            valid_board_solution = False
    return valid_board_solution

def validate_set(block_set):
    validator_set = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    valid_set = False
    if set(validator_set).issubset(block_set) and len(set(block_set)) == 9:
        valid_set = True
    return valid_set


def get_columns_as_rows(board):
    board_columns = [[] for i in range(9)]
    for row_index, row in enumerate(board):
        for block_index, block_element in enumerate(board[row_index]):
            board_columns[block_index].append((board[row_index][block_index]))
    return board_columns


def get_block_sets_as_rows(board):
    board_block_sets = []
    for x_coord in range(0,9, 3):
        for y_coord in range(0, 9, 3):
            row = []
            for i in range(0+y_coord, 3+y_coord):
                row.extend(board[i][0+x_coord:3+x_coord])
            board_block_sets.append(row)
    return board_block_sets

@test.it('Test Cases')
def example_test_case():
    test.assert_equals(valid_solution([
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]), True)

    test.assert_equals(valid_solution([
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 0, 3, 4, 9],
        [1, 0, 0, 3, 4, 2, 5, 6, 0],
        [8, 5, 9, 7, 6, 1, 0, 2, 0],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 0, 1, 5, 3, 7, 2, 1, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 0, 0, 4, 8, 1, 1, 7, 9]
    ]), False)

    test.assert_equals(valid_solution([
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [9, 1, 2, 3, 4, 5, 6, 7, 8]
    ]), False)

