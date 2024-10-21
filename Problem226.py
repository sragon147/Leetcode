from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root.left is None and root.right is None:
            return None
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        root.left, root.right = root.right, root.left
        return root

invertTree =Solution().invertTree((TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))))