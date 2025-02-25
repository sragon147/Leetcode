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
        c = 1
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
              c -= 1
            if c < 0:
              if nums[l] == 0:
                c += 1
              l += 1
            print(l, r, c)
        return r - l
    
print(Solution().longestSubarraySlidingWindow([0,1,1,1,0,1,1,0,1]))