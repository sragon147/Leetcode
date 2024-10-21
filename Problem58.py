class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        for i, char in enumerate(s[::-1]):
            if char == ' ':
                return i
result = Solution().lengthOfLastWord("Hello World") # 5
print(result) # 5