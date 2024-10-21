from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = r = 0
        flip = 0
        while r < len(nums):
            if nums[r] == 0:
                flip += 1
            if flip > k:
                if nums[l] == 0:
                    flip -= 1
                l += 1
            r += 1
        return r-l

print(Solution().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)) # 6