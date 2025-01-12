from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
                
    def maxArea(self, height: List[int]) -> int:
        r_pointer = len(height)-1
        l_pointer = 0
        high = 0
        while (l_pointer != r_pointer):
            if height[l_pointer] < height[r_pointer]:
                high = max(high, height[l_pointer]*(r_pointer-l_pointer))
                l_pointer = l_pointer + 1
                print(high, l_pointer)

            else:
                high = max(high, height[r_pointer]*(r_pointer-l_pointer))
                r_pointer = r_pointer - 1
                print(high, r_pointer)