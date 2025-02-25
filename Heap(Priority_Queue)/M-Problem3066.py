import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        count = 0
        while len(nums) > 1:
            if nums[0] >= k:
                break
            min_1 = heapq.heappop(nums)
            min_2 = heapq.heappop(nums)
            heapq.heappush(nums, min_1 * 2 + min_2)
            count += 1
        return count