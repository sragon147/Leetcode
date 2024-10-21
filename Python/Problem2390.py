class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        for char in s:
            if char != '*':
                res.append(char)
            else:
                res.pop()
        return ''.join(res)