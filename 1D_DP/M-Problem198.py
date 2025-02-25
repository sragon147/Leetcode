from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prev2, prev1 = 0, nums[0]
        for i  in range(1, len(nums)):
            max_money = max(prev2+nums[i], prev1)
            prev2, prev1 = prev1, max_money
            print(prev2, prev1, max_money)

Solution().rob([0,0])
