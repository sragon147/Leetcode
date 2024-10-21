from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sum = 0
        for i in nums:
            sum ^= i
        return sum
        
                