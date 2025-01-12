import heapq
from typing import List
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        top_candidates = []
        last_candidates = []
        top = 0
        last = len(costs) - 1
        total = 0
        while k > 0:
            while len(top_candidates) < candidates and top <= last:
                heapq.heappush(top_candidates, costs[top])
                top += 1
            
            while len(last_candidates) < candidates and top <= last:
                heapq.heappush(last_candidates, costs[last])
                last -= 1

            top_min_candidate = top_candidates[0] if top_candidates else float('inf')
            last_min_candidate = last_candidates[0] if last_candidates else float('inf')
            
            if top_min_candidate <= last_min_candidate:
                total += top_min_candidate
                heapq.heappop(top_candidates)
            else:
                total += last_min_candidate
                heapq.heappop(last_candidates)

            k -= 1
        return total

Solution().totalCost([17,12,10,2,7,2,11,20,8], 3, 4)