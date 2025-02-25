from typing import List
class Solution:
    def jumpGame(self, nums: List[int]) -> bool:
        n = len(nums)
        maxPos = 0
        for i in range(n):
            if i > maxPos:
                return False
            maxPos = max(maxPos, i + nums[i])
            if maxPos >= n - 1:
                return True
        return False
    def jumpGame2(self, nums: List[int]) -> bool:
        g = nums[0]
        for i in range(1, len(nums)):
            if g < 0:
                return False
            if g < nums[i]:
                g = nums[i]
            g -= 1
        return True

Solution().jumpGame([2,3,1,1,4])