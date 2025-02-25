from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return 
        
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] <= nums[r]: return nums[l]
            m = l + (r - l) // 2
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m
        return nums[l]
    
    def findMin2(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + (r - l) // 2
            if nums[m] <= nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]
Solution().findMin2([2, 1])