from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        def helper(num):
            count = 0
            while num != 0:
                if num & 1:
                    count += 1
                num >>= 1
            return count
                
        ans = []
        for i in range(n+1):
            ans.append(helper(i))
        return ans
    
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        res = [0] * (n + 1)
        for i in range(n + 1):
            res[i] = res[i // 2] + i % 2
        return res

Solution().countBits(5)