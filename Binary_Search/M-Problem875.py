from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(speed) -> bool:
            sum = 0
            for pile in piles:
                sum += (pile - 1) // speed + 1
            return sum <= h
        
        l, r = 1, max(piles)

        while l < r:
            m = l + (r - l) // 2
            if feasible(m):
                r = m
            else:
                l = m + 1
        return l
    