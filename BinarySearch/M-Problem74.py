from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = l + (r - l) // 2
            if matrix[m][0] < target:
                l = m + 1
            elif matrix[m][0] > target:
                r = m - 1
            else:
                return True
        found_row = l - 1
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = l + (r - l) // 2
            if matrix[found_row][m] < target:
                l = m + 1
            elif matrix[found_row][m] > target:
                r = m - 1
            else:
                return True
        return matrix[found_row][l-1] == target
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows * cols - 1
        while l <= r:
            m = l + (r - l) // 2
            if matrix[m // cols][m % cols] < target:
                l = m + 1
            elif matrix[m // cols][m % cols] > target:
                r = m - 1
            else:
                return True
        return False
    
    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        n, m = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1

        while l != r:
            mid = l + (r - l) // 2
            if matrix[mid // m][mid % m] < target:
                l = mid + 1
            else:
                r = mid

        return matrix[r // m][r % m] == target
Solution().searchMatrix2([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)