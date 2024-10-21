from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(root, is_left, length):
            if root == None:
                return length - 1
            if is_left:
                return max(dfs(root.left, False, length + 1), dfs(root.right, True, 1))
            else:
                return max(dfs(root.right, True, length + 1), dfs(root.left, False, 1))
        return max(dfs(root.left, False, 1), dfs(root.right, True, 1))
Solution().longestZigZag(TreeNode(1, None, TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(1)), None))) # 3