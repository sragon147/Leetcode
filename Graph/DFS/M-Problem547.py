from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        count = 0
        for i in range(n):
            if not visited[i]:
                print(i)
                self.dfs(isConnected, i, visited)
                print(visited)
                count += 1
        return count
    def dfs(self, isConnected, i, visited):
        visited[i] = True
        for j in range(len(isConnected)):
            if isConnected[i][j] == 1 and not visited[j]:
                print(i, j)
                self.dfs(isConnected, j, visited)
                    
Solution().findCircleNum([[1,1,0],[1,1,1],[0,1,1]])