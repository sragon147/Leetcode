from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                # index is the position of temperature that could not find the temp larger than it
                index = stack.pop()
                res[index] = i - index
            stack.append(i)
        return res
        
Solution().dailyTemperatures([73,74,75,71,69,72,76,73])