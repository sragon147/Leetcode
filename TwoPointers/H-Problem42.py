from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        max_l = max_r = 0
        while l <= r:
            if height[l] <= height[r]:
                if height[l] >= max_l:
                    max_l = height[l]
                res += max_l - height[l]
                l += 1
            else:
                if height[r] >= max_r:
                    max_r = height[r]
                res += max_r - height[r]
                r -= 1
        return res
    
Solution().trap2([0,1,0,2,1,0,1,3,2,1,2,1])