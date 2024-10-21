from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = []
        for num in nums:
            if num in seen:
                return True
            seen.append(num)
        return False