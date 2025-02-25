from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        bucket = [0] * (n + 1)
        for c in citations:
            if c >= n:
                bucket[n] += 1
            else:
                bucket[c] += 1
        
        print(bucket)
        sum_ = 0
        for b in range(n, -1, -1):
            sum_ += bucket[b]
            if b <= sum_:
                return b
        return 0
Solution().hIndex([3,0,6,5,1]) # 3