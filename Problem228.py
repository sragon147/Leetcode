from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        slow = 0
        fast = 0
        ranges = {}
        while fast < len(nums):
            if nums[fast] - nums[slow] == fast - slow:
                ranges[nums[slow]] = nums[fast]
                fast += 1
            else:
                slow = fast
        return [f"{k}->{v}" if k != v else str(k) for k, v in ranges.items()] 