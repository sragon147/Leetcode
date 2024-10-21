class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        column = ""
        while columnNumber > 0:
            column = chr(ord('A') + ((columnNumber-1) % 26)) + column
            columnNumber = (columnNumber - 1) // 26
        return column
    
title = Solution().convertToTitle(1)
print(title) # A