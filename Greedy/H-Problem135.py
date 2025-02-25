from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        out = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                out[i] = out[i-1] + 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i+1]:
                out[i] = max(out[i], out[i+1] + 1)
        return sum(out)
    
    def candy2(self, ratings: List[int]) -> int:
        i = 1
        n = len(ratings)
        res = 0
        while i < n:
            if ratings[i] == ratings[i-1]:
                i += 1
                continue
            peak = 0
            while ratings[i] < ratings[i-1]:
                peak += 1
                res += peak
                i += 1
                if i == n-1:
                    return res
            
            valley = 0
            while i < n and ratings[i] > ratings[i+1]:
                valley += 1
                res += valley
                i += 1
            
            res -= min(peak, valley)
        return res


Solution().candy2([1,3,5,4,3,2,1,2])