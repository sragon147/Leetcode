class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        count = 0
        def dfs(r, c):
            nonlocal count
            if obstacleGrid[r][c] == 1:
                return
            if r == rows-1 and c == cols-1:
                count += 1
                return
            obstacleGrid[r][c] = 1
            if c + 1 < cols: dfs(r, c + 1)
            if r + 1 < rows: dfs(r + 1, c)
            obstacleGrid[r][c] = 0
        dfs(0,0)
        return count
    
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        cur = [0] * cols
        cur[0] = 1
        for c in range(1, cols):
            cur[c] = cur[c-1] if obstacleGrid[0][c] == 0 else 0
        for r in range(1, rows):
            cur[0] = cur[0] if obstacleGrid[r][0] != 1 else 0
            for c in range(1, cols):
                cur[c] = cur[c] + cur[c-1] if obstacleGrid[r][c] == 0 else 0
        
        return cur[-1]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        obstacleGrid[0][0] = 1

        for c in range(1,n):
            if obstacleGrid[0][c] == 1:
                obstacleGrid[0][c] = 0
            else:
                obstacleGrid[0][c] = obstacleGrid[0][c-1]
        
        for r in range(1,m):
            if obstacleGrid[r][0] == 1:
                obstacleGrid[r][0] = 0
            else:
                obstacleGrid[r][0] = obstacleGrid[r-1][0]
        
        for r in range(1,m):
            for c in range(1,n):
                if obstacleGrid[r][c] == 0:
                    obstacleGrid[r][c] = obstacleGrid[r-1][c] + obstacleGrid[r][c-1]
                else:
                    obstacleGrid[r][c] = 0

        return obstacleGrid[-1][-1]