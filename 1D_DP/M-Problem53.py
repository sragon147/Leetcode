class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        final_max = float('-inf')
        curr_max = 0

        for num in nums:
            curr_max = max(num, curr_max + num)
            final_max = max(final_max, curr_max)

        return final_max
    
    def maxSubArray(self, nums):
        dp = [*nums]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
        return max(dp)