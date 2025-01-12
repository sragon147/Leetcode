class Solution(object):
    def twoSum(self, nums, target):
        for i, num in enumerate(nums):
            pair_num = target - num
            if pair_num in nums[i+1:]:
                index = nums.index(pair_num, i+1)
                return [i, index]
        return []