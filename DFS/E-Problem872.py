from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode]) -> List:
        if root == None:
            return []
        if root.left or root.right:
            left = self.dfs(root.left)
            right = self.dfs(root.right)
        else:
            return [root.val]
        return left + right
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1 = []
        leaf2 = []
        self.dfs(root1, leaf1)
        self.dfs(root2, leaf2)
        return leaf1 == leaf2