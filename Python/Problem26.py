from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        duplicate_dict = {}
        for i in nums:
            if i not in duplicate_dict:
                duplicate_dict[i] = 1
            else:
                duplicate_dict[i] += 1
        k = len(duplicate_dict)
        nums = list(duplicate_dict.keys())
        print(nums)
        return k
    
Solution.removeDuplicates(Solution, [1,1,2])