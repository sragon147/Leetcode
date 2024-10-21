from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        row = [0] * (rowIndex + 1)
        row[0], row[-1] = 1, 1
        for i in range(1, rowIndex//2 + 1):
            row[i] = self.getRow(rowIndex - 1)[i-1] + self.getRow(rowIndex - 1)[i]
            row[rowIndex - i] = row[i]
        print(row)
        return row
    
Solution().getRow(4) # [1,3,3,1]