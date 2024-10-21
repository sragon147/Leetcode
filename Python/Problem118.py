from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            row = [0] * (i + 1)
            row[0], row[-1] = 1, 1
            for j in range(1, i//2 + 1):
                row[j] = result[i-1][j-1] + result[i-1][j]
                row[i-j] = row[j]
            result.append(row)
        return result

print(Solution().generate(5))