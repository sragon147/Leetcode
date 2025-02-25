from collections import defaultdict
import heapq
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits), key=lambda x: x[0])
        
        max_heap = []
        available_projects = 0
        for _ in range(k):
            while available_projects < len(projects) and projects[available_projects][0] <= w:
                heapq.heappush(max_heap, -projects[available_projects][1])
                available_projects += 1

            if max_heap:
                w -= heapq.heappop(max_heap)
            else:
                break
       
        return w

Solution().findMaximizedCapital(2, 0, [1,2,3], [0,1,1])