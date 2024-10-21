from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode], leaves: List[int]) -> None:
        if root.left != None:
            self.traverseTree(root.left,leaves)
        if root.right != None:
            self.traverseTree(root.right,leaves)
        if(root.left == None and root.right == None):
            leaves.append(root.val)
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1 = []
        leaf2 = []
        self.dfs(root1, leaf1)
        self.dfs(root2, leaf2)
        return leaf1 == leaf2