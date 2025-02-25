from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(0, len(triangle) - 1):
            for j in range(1, len(triangle[i])):
                triangle[i+1][j] += min(triangle[i][j-1], triangle[i][j])
            triangle[i+1][0] += triangle[i][0]
            triangle[i+1][-1] += triangle[i][-1]

        return min(triangle[-1])
    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1]

        for row in triangle[::-1][1:]:
            for i in range(len(row)):
                dp[i] = min(dp[i], dp[i + 1]) + row[i]
        
        return dp[0]
    
    def minimumTotal3(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])

        return triangle[0][0]
Solution().minimumTotal3([[2],[3,4],[6,5,7],[4,1,8,3]])