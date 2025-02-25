from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        l, r = 0, len(nums)
        while l < r:
            m = l + (r - l) // 2
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
        if l >= len(nums) or nums[l] != target:
            return [-1, -1]
        left = l
        r = len(nums)
        while l < r:
            m = l + (r - l) // 2 + 1
            if nums[m] > target:
                r = m - 1
            else:
                l = m
        if r < 0 or nums[r] != target:
            return [-1, -1]
        return [left, r]
    def searchRange(self, nums, target):
        def search(lo, hi):
            if nums[lo] == target == nums[hi]:
                return [lo, hi]
            if nums[lo] <= target <= nums[hi]:
                mid = (lo + hi) / 2
                l, r = search(lo, mid), search(mid+1, hi)
                return max(l, r) if -1 in l+r else [l[0], r[1]]
            return [-1, -1]
        return search(0, len(nums)-1)
    
Solution().searchRange([1], 1)