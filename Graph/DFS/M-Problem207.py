from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_dict ={}
        for pre in prerequisites:
            if pre[0] in pre_dict:
                pre_dict[pre[0]].append(pre[1])
            else:
                pre_dict[pre[0]] = [pre[1]]

        def take(c, w, t):
            if c in w:
                return False
            if c in t:
                return True
            w.add(c)
            for p in pre_dict[c]:
                if not take(p, w, t):
                    return False
            w.remove(c)
            t.add(c)
            return True

        took = set()
        wait = set()
        for course in range(numCourses):
            if not take(course, wait, took):
                return False
        return len(took) == numCourses
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.graph = defaultdict(list)
        for p in prerequisites:
            self.graph[p[0]].append(p[1])
        nodes = list(self.graph.keys())
        self.visited = set()
        for node in nodes:
            self.visiting = set()
            if not self.dfs(node):
                return False
        return True

    def dfs(self, node):
        if node in self.visited:
            return True
        if node in self.visiting:
            return False
        self.visiting.add(node)
        for n in self.graph[node]:
            if not self.dfs(n):
                return False
        self.visited.add(node)
        return True
    
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
        return len(bfs) == numCourses

Solution().canFinish(2, [[1,0]])