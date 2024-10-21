from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        result = []
        for i in nums:
            if i != val:
                result.append(i)
        return len(result)