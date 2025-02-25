from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        while root:
            if not root.left:
                root = root.right
                continue
            tail = root.left
            while tail.right:
                tail = tail.right
            tail.right = root.right

            root.right = root.left
            root.left = None

            root = root.right
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = prev
        root.left = None
        prev = root


Solution().flatten(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6))))