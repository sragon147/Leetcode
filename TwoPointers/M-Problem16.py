from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff = float('inf')
        ans = 0
        for i in range(len(nums)-2):
            r = len(nums)-1
            l = i+1
            while(l < r):
                total = nums[i]+nums[l]+nums[r]
                diff = abs(total-target)
                if diff < min_diff:
                    min_diff = diff
                    ans = total
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    return total
        return ans