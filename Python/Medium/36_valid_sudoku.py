"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Constraints:

    board.length == 9
    board[i].length == 9
    board[i][j] is a digit 1-9 or '.'.
"""

#spaghetti, first draft
def solution(sudoku: list) -> bool:

    #squares
    box = []
    box2 = []
    box3 = []

    # columns and rows
    for i in range(len(sudoku)):
        column_numerals = []
        row_numerals = []
        for x in range(len(sudoku)):

            row_box_value = sudoku[i][x]
            col_value = sudoku[x][i]

            if col_value != "." and col_value in column_numerals:
                return False
            elif row_box_value != "." and row_box_value in row_numerals:
                return False
            
            elif x < 3:
                if row_box_value != "." and row_box_value in box:
                    return False
                else:
                    box.append(row_box_value)
            elif x >= 3 and x < 6:
                if row_box_value != "." and row_box_value in box2:
                    return False
                else:
                    box2.append(row_box_value)

            else:
                if row_box_value != "." and row_box_value in box3:
                    return False
                else:
                    box3.append(row_box_value)

            column_numerals.append(col_value)
            row_numerals.append(row_box_value)

        if i == 2 or i == 5:
            box.clear()
            box2.clear()
            box3.clear()


    return True

#Slower than original lol...
def solution_cleaned(sudoku: list):
    rows = [set() for x in range(9)]
    cols = [set() for x in range(9)]
    squares = [[set() for x in range(3)] for i in range(3)]
    for x in range(9):
        for y in range(9):
            val = sudoku[x][y]
            if val == ".":
                continue
            if val in rows[x] or val in cols[y] or val in squares[x//3][y//3]:
                return False

            rows[x].add(val)
            cols[y].add(val)
            squares[x//3][y//3].add(val)

    return True



if __name__ == '__main__':
    sudoku = [[".","2",".",".",".",".",".",".","."],
              [".",".",".",".",".",".","5",".","1"],
              [".",".",".",".",".",".","8","1","3"],
              ["4",".","9",".",".",".",".",".","."],
              [".",".",".",".",".",".",".",".","."],
              [".",".","2",".",".",".",".",".","."],
              ["7",".","6",".",".",".",".",".","."],
              ["9",".",".",".",".","4",".",".","."],
              [".",".",".",".",".",".",".",".","."]]

    print(solution_cleaned(sudoku))


