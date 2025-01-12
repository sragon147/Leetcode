from typing import List
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for (num, den), val in zip(equations, values):
            if num in graph:
                graph[num][den] = val
            else:
                graph[num] = {den: val}
            if den in graph:
                graph[den][num] = 1 / val
            else:
                graph[den] = {num: 1 / val}
        def dfs(num, den, visited):
            print(num, den, visited)
            if num not in graph or den not in graph:
                return -1
            if num == den:
                return 1
            visited.add(num)
            for next_num in graph[num]:
                if next_num in visited:
                    continue
                visited.add(next_num)
                val = dfs(next_num, den, visited)
                if val != -1:
                    return val * graph[num][next_num]
                visited.remove(next_num)
            return -1
        return [dfs(num, den, set()) for num, den in queries]
Solution().calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])