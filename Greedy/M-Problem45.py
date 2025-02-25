from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        dp = [0] * n
        for i in range(1, n):
            dp[i] = min([dp[j] + 1 for j in range(i) if j + nums[j] >= i])
        return dp[-1]
    def jump(self, nums: List[int]) -> int:
        current_max = 0
        jumps = 0
        full_max = 0
        for i in range(len(nums)-1):
            if full_max < i + nums[i]:
                full_max = i + nums[i]
            if current_max == i:
                jumps+=1
                current_max = full_max
        return jumps
                
Solution().jump([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3])