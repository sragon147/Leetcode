from collections import defaultdict
from typing import List
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        m = defaultdict(int)
        cnt = 0

        for row in grid:
            m[str(row)] += 1
        print(m)
        
        for i in range(len(grid[0])):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            cnt += m[str(col)]
        return cnt

print(Solution().equalPairs([[3,1,2,2],[1,4,4,4],[2,4,2,2],[2,5,2,2]]))