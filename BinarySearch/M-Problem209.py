from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0 if nums[0] < target else 1
        l, r = 0, 1
        cur_sum = nums[l] + nums[r]
        res = len(nums) + 1
        for _ in range(2*len(nums)):
            if cur_sum < target: 
                if r < len(nums) - 1:
                    r += 1
                    cur_sum += nums[r]
            else:
                res = min(res, r - l + 1)
                if l < len(nums):
                    cur_sum -= nums[l]
                    l += 1
        return 0 if res == len(nums) + 1 else res
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        currAns = 0

        left = 0

        for right in range(len(nums)):
            currAns += nums[right]

            while currAns >= target:

                if currAns >= target:
                    ans = min(ans, right - left + 1)
                    
                currAns -= nums[left]
                left += 1


        if ans == float('inf'):
            return 0

        return ans
Solution().minSubArrayLen(15, [1,2,3,4,5])