from collections import deque
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bfs(self, root, result, level=0):
        if not root:
            return
        if len(result) == level:
            result.append(root.val)
        self.bfs(root.right, result, level + 1)
        self.bfs(root.left, result, level + 1)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.bfs(root, result)
        return result
    def rightSideViewI(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root: return
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left) 
                if node.right:
                    queue.append(node.right)
            ans.append(node.val)
        return ans

Solution().rightSideViewI(TreeNode(1, TreeNode(2, None, TreeNode(5)))) # [1, 3, 4]