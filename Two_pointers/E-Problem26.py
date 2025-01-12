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
    
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1

        for j in range(1, len(nums)):
            if nums[j] != nums[i - 1]:
                nums[i] = nums[j]
                i += 1
        
        return i
    
Solution.removeDuplicates(Solution, [1,1,2])
