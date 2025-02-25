class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        A = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            A[a].append(b)
        visited, cycle = set(), set()

        res = []
        def dfs(node):
            if node in cycle:
                return False
            
            if node in visited:
                return True
            
            cycle.add(node)

            for child in A[node]:
                if not dfs(child):
                    return False

            cycle.remove(node)
            visited.add(node)
            res.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        bfs =[i for i in range(numCourses) if in_degree[i] == 0]
        for i in bfs:
            for j in graph[i]:
                in_degree[j] -= 1
                if in_degree[j] == 0:
                    bfs.append(j)
        return bfs if len(bfs) == numCourses else []