from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValid(x: int, y:int, nums: List[int]) -> bool:
            if board[x][y] in nums:
                return False
            nums.append(board[x][y])
            return True
        for i in range(9):
            dictRow = []
            for j in range(9):
                if board[i][j] == ".":
                    continue
                isRowValid = isValid(i, j, dictRow)
                if not isRowValid:
                    return False
            dictCol = []
            for j in range(9):
                if board[j][i] == ".":
                    continue
                isColValid = isValid(j, i, dictCol)
                if not isColValid:
                    return False
            dictBox = []
            for j in range(9):
                x = 3*(i//3) + j//3
                y = 3*(i%3) + j%3
                if board[x][y] == ".":
                    continue
                isBoxValid = isValid(x, y, dictBox)
                if not isBoxValid:
                    return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        grid_set = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                    
                if board[i][j] in row_set[i] or board[i][j] in col_set[j] or board[i][j] in grid_set[i//3][j//3]:
                    return False
                row_set[i].add(board[i][j])
                col_set[j].add(board[i][j])
                grid_set[i//3][j//3].add(board[i][j])
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]

        # label boxes 0 - 8, left to right, top to bottom
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                
                digit = int(board[row][col])
                if digit in cols[col]:
                    return False
                
                cols[col].add(digit)

                if digit in rows[row]:
                    return False
                
                rows[row].add(digit)

                currBox = ((row // 3)*3) + (col // 3)
                if digit in boxes[currBox]:
                    return False
                
                boxes[currBox].add(digit)
    
        return True

Solution().isValidSudoku(
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])