from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] > nums[m-1] and nums[m] > nums[m+1]:
                return m 
            elif nums[m] < nums[m-1]:
                r = m - 1
            elif nums[m] < nums[m+1]:
                l = m + 1 
    def findPeakElement2(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[m+1]:
                l = m + 1
            else:
                r = m
        return l
Solution().findPeakElement2([1,6,3,2,5,3,4])