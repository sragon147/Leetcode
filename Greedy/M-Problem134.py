from typing import List
from collections import deque
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l = r = 0
        cur_gas = 0
        while r - l < len(gas):
            if cur_gas + gas[r] - cost[r] < 0:
                l -= 1
                cur_gas += gas[l] - cost[l]
            else:
                cur_gas += gas[r] - cost[r]
                r += 1
        if cur_gas < 0:
            return -1
        return r % len(gas)
    
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        tank = 0
        start = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start = i +1
        return start

print(Solution().canCompleteCircuit([2,3,4], [3,4,3]))
