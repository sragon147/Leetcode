from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.dfs(root, result)
        return result
    def dfs (self, root: Optional[TreeNode], result: List[int]):
        if root is None:
            return
        self.dfs(root.left,result)
        self.dfs(root.right,result)
        result.append(root.val)

r = Solution().postorderTraversal(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7))) )
print(r) # [4, 5, 2, 6, 7, 3, 1]