from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtracking(path, l, r):
            if len(path) == 2 * n:
                res.append("".join(path.copy()))
                return
            
            if r < l and r < n:
                path.append(")")
                backtracking(path, l, r + 1)
                path.pop()        
            if l < n:
                path.append("(")
                backtracking(path, l + 1, r)
                path.pop()

        backtracking([], 0, 0)
        return res
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(l, r, t):
            if l > n or r > n or l < r:
                return
            if l == n and r == n:
                ans.append(t)
                return
            dfs(l + 1, r, t + '(')
            dfs(l, r + 1, t + ')')

        ans = []
        dfs(0, 0, '')
        return ans
    
Solution().generateParenthesis(3)