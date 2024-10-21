from typing import List
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = [False] * (n)
        visited[0] = True
        count = [0]
        for i in range(n - 1):
            if not (visited[connections[i][0]] and visited[connections[i][1]]):
                self.dfs(connections, i, visited, count)
        return count[0]
        
    def dfs(self, connections, i, visited, count):
        if not visited[connections[i][0]] and not visited[connections[i][1]]:
            self.dfs(connections, i + 1, visited, count)
        if visited[connections[i][0]]:
            connections[i][0], connections[i][1] = connections[i][1], connections[i][0]
            count[0] += 1
        visited[connections[i][0]] = True

    def minReorder2(self, n: int, connections: List[List[int]]) -> int:
        
        connected = {0}
        counter = 0
        stack = []

        while connections:
            a, b = connections.pop()
            if b in connected: 
                connected.add(a)
            elif a in connected:
                counter += 1 
                connected.add(b)
            else:
                stack.append((a,b))
            
            if not connections:
                connections = stack
                stack = []
        
        return counter
Solution().minReorder(5, [[1,0],[1,2],[3,2],[3,4]])