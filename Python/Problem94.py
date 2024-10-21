from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.dfs(root, result)
        return result
    
    def dfs(self, root: Optional[TreeNode], result: List[int]):
        if root is None:
            print(result)
            return
        self.dfs(root.left, result)
        result.append(root.val)
        self.dfs(root.right, result)

Solution().inorderTraversal(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7))))