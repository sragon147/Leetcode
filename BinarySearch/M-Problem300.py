import bisect
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for x in nums:
            if len(sub) == 0 or sub[-1] < x:
                sub.append(x)
            else:
                idx = bisect.bisect_left(sub, x)
                sub[idx] = x
        return len(sub)
    
    def pathOfLIS(self, nums: List[int]):
        sub = []
        subIndex = []  # Store index instead of value for tracing path purpose
        trace = [-1] * len(nums)  # trace[i] point to the index of previous number in LIS
        for i, x in enumerate(nums):
            if len(sub) == 0 or sub[-1] < x:
                if subIndex:
                    trace[i] = subIndex[-1]
                sub.append(x)
                subIndex.append(i)
            else:
                idx = bisect.bisect_left(sub, x)  # Find the index of the smallest number >= x, replace that number with x
                if idx > 0:
                    trace[i] = subIndex[idx - 1]
                sub[idx] = x
                subIndex[idx] = i

        path = []
        t = subIndex[-1]
        while t >= 0:
            path.append(nums[t])
            t = trace[t]
        return path[::-1]

Solution().pathOfLIS([10,9,2,5,3,7,101,18])