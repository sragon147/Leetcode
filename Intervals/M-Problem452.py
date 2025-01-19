from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        shot_e = points[0][1]
        a = 1
        for i in range(1, len(points)):
            if points[i][0] > shot_e:
                a += 1
                shot_e = points[i][1]
        return a

Solution().findMinArrowShots([[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]])

