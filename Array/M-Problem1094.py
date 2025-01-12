from typing import List
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        fr_to = []
        for trip in trips:
            fr_to.append([trip[1], trip[0]])
            fr_to.append([trip[2], -trip[0]])
            
        fr_to = sorted(fr_to)

        for i, j in fr_to:
            capacity -= j
            if capacity < 0:
                return False
        return True
  
Solution().carPooling([[2,1,5],[3,3,7]], 5)