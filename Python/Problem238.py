from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ltor = [1] * len(nums)
        res = 1
        for i in range(1, len(nums)):
            ltor[i] = ltor[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            res *= nums[i+1]
            ltor[i] *= res
        return ltor

result = Solution().productExceptSelf([1,2,3,4])