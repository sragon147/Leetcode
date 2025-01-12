from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = []
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                if grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        while queue:
            x, y, minutes = queue.pop(0)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    fresh -= 1
                    if fresh == 0:
                        return minutes + 1
                    queue.append((nx, ny, minutes + 1))
                    grid[nx][ny] = 2
        return -1