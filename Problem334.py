from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        a = b = float('inf')
        for num in nums:
            if num <= a:
                a = num
            elif num <= b:
                b = num
            else:
                return True
        return False

print(Solution().increasingTriplet([2,1,5,0,4,6]))