from typing import List
from collections import deque

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = deque()
        res.append([])
        out = []
        while res and len(res[0]) <= k:
            stack = res.popleft()
            if stack:
                cur_sum = stack.pop()
                last_num = stack[-1] + 1
            else:
                cur_sum = 0
                last_num = 1
            for i in range(last_num,10):
                if cur_sum + i > n:
                    continue
                if len(stack) == k-1:
                    if cur_sum + i == n:
                        out.append(stack + [i])
                else:
                    res.append(stack + [i] + [cur_sum + i])
        return out
    
    def combinationSum3Backtracking(self, k, n):
        ret = []
        self.dfs(1, k, n, [], ret)
        print(ret)
        return ret
    
    def dfs(self, start, k, n, path, ret):
        print(path)
        if k < 0 or n < 0:
            return
        if k == 0 and n == 0:
            ret.append(path)
            return
        for i in range(start, 10):
            self.dfs(i+1, k-1, n-i, path+[i], ret)
    
Solution().combinationSum3Backtracking(3, 7)