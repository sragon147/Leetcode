from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:  
            return 0
        # Initialize the depth of two subtrees...
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)
        # If the both subtrees are empty...
        if root.left is None and root.right is None:
            return 1
        # If the left subtree is empty, return the depth of right subtree after adding 1 to it...
        if root.left is None:
            return 1 + rightDepth
        # If the right subtree is empty, return the depth of left subtree after adding 1 to it...
        if root.right is None:
            return 1 + leftDepth
        # When the two child function return its depth...
        # Pick the minimum out of these two subtrees and return this value after adding 1 to it...
        return min(leftDepth, rightDepth) + 1  # Adding 1 is the current node which is the parent of the two subtrees...

result = Solution().minDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
print(result) # Expected output: 3