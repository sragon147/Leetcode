from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = r = 0
        left_sub = 0
        all_ones = True
        max_sub = 0
        while r < len(nums):
            # print(l, r)
            if nums[r] != 1:
                all_ones = False
                print(l, r, left_sub, r-l)
                max_sub = max(max_sub, left_sub + r - l)
                left_sub = r-l
                l = r + 1
            r += 1
        print(l, r, left_sub, r-l)
        max_sub = max(max_sub, left_sub + r - l)
        if all_ones:
            return max_sub - 1
        return max_sub
    def longestSubarraySlidingWindow(self, nums: List[int]) -> int:
        k = 1
        i = 0
        for j in range(len(nums)):
            if nums[j] == 0:
              k -= 1
            if k < 0:
              if nums[i] == 0:
                k += 1
              i += 1
            print(i, j, k)
        return j - i
    
print(Solution().longestSubarraySlidingWindow([0,1,1,1,0,1,1,0,1]))