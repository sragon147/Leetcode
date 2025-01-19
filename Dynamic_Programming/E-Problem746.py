from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        oneStairAway, twoStairAway = 0, 0
        for i in range(2,len(cost)+1):
            total = min(oneStairAway + cost[i-1], twoStairAway + cost[i-2])
            twoStairAway, oneStairAway, = oneStairAway, total
        return total

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prev, cur = cost[0], cost[1]
        for i in range(2,n):
            dpi = cost[i] + min(prev, cur)
            prev, cur = cur, dpi
        return min(prev, cur)

print(Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))