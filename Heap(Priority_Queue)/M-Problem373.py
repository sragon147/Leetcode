import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        queue = []
        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
        push(0, 0)
        pairs = []
        while queue and len(pairs) < k:
            _, i, j = heapq.heappop(queue)
            pairs.append([nums1[i], nums2[j]])
            push(i, j + 1)
            if j == 0:
                push(i + 1, 0)
        return pairs
    
    def kSmallestPairs(self, nums1, nums2, k):
        res = []
        if not nums1 or not nums2 or not k:
            return res
        
        heap = []
        visited = set()
        
        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))
        
        visited.add((0, 0))
        
        while len(res) < k and heap:
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            
            if i+1 < len(nums1) and (i+1, j) not in visited:
                heapq.heappush(heap, (nums1[i+1] + nums2[j], i+1, j))
                visited.add((i+1, j))
            
            if j+1 < len(nums2) and (i, j+1) not in visited:
                heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1))
                visited.add((i, j+1))
        return res
Solution().kSmallestPairs([1,7,11], [2,4,6], 7)