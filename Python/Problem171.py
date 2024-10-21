class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        column = 0
        for title in columnTitle:
            column = column*26 + ord(title) - ord('A') + 1
        return column

title = Solution().titleToNumber("ZY")
print(title) # 1
