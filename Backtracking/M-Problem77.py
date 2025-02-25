from collections import deque
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return []
        
        stack = deque()
        for i in range(0, n - k + 1):
            stack.append([i+1])

        while len(stack[0]) < k:
            s = stack.popleft()
            start = s[-1]
            end = n - k + len(s) + 1
            for i in range(start, end):
                stack.append(s + [i + 1])
        return list(stack)

    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(start, path):
            if len(path) == k:
                result.append(path.copy())
                return
            
            for i in range(start, n - (k - len(path)) + 1):
                path.append(i+1)
                backtrack(i+1, path)
                path.pop()
        
        backtrack(0, [])
        return result
    
    def combine(self, n, k):
        combs = [[]]
        
        for _ in range(k):
            new_combs = []
            for comb in combs:
                for i in range(1, n + 1):
                    if not comb or i > comb[-1]:
                        new_combs.append([i] + comb)
            combs = new_combs
        
        return combs

    def combine2(self, n: int, k: int):
        result = []
        i = 0
        p = [0] * k
        
        while i >= 0:
            print(p)
            p[i] += 1
            if p[i] > n:
                i -= 1
            elif i == k - 1:
                result.append(p[:])
            else:
                i += 1
                p[i] = p[i - 1]
                
        return result

Solution().combine2(4, 3)
