from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m1 = l + (r - l) // 2
            m2 = m1 + 1
            if nums[m1] < nums[m2]:
                l = m2
            else:
                r = m1
        return l

Solution().findPeakElement([1,2,3,1])
