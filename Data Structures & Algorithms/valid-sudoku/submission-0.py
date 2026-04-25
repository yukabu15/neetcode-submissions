class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sudoku = [[set() for _ in range(9)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                if num in sudoku[0][i]:
                    return False
                else:
                    sudoku[0][i].add(num)
                if num in sudoku[1][j]:
                    return False
                else:
                    sudoku[1][j].add(num)
                square_group = i//3 * 3 + j//3
                if num in sudoku[2][square_group]:
                    return False
                else:
                    sudoku[2][square_group].add(num)
        
        return True