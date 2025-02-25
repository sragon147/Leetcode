from typing import List   
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if not matrix or not matrix[0]:
            return result
        compass = ((0, 1), (1, 0), (0, -1), (-1, 0))
        direction = 0
        steps = [len(matrix[0]), len(matrix) - 1]
        row, col = 0, -1
        while steps[direction%2]:
            for _ in range(steps[direction%2]):
                row += compass[direction][0]
                col += compass[direction][1]
                result.append(matrix[row][col])
            steps[direction%2] -= 1
            direction = (direction + 1) % 4
        return result
    def spiralOrder(self, matrix):
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
    def spiralOrder(self, matrix):
        result = []
        if not matrix or not matrix[0]:
            return result
        
        row_start, row_end = 0, len(matrix) - 1
        col_start, col_end = 0, len(matrix[0]) - 1

        while row_start <= row_end and col_start <= col_end:
            for i in range(col_start, col_end + 1):
                result.append(matrix[row_start][i])
            row_start += 1
            
            for i in range(row_start, row_end + 1):
                result.append(matrix[i][col_end])
            col_end -= 1

            if (row_start > row_end or col_start > col_end):
                break
            
            for i in range(col_end, col_start - 1, -1):
                result.append(matrix[row_end][i])
            row_end -= 1

            for i in range(row_end, row_start - 1, -1):
                result.append(matrix[i][col_start])
            col_start += 1
        return result

        
Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]])