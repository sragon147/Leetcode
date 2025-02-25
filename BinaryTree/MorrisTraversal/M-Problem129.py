from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([(root, 0)])
        res = 0
        while q:
            node, val = q.pop()
            if not node.left and not node.right:
                res += val * 10 + node.val
            if node.left:
                q.append((node.left, val * 10 + node.val))
            if node.right:
                q.append((node.right, val * 10 + node.val))

    def sumPaths(self, root, s) -> int:
        s += root.val
        if not root.left and not root.right:
            return s
        nl = self.sumPaths(root.left, s*10) if root.left else 0
        nr = self.sumPaths(root.right, s*10) if root.right else 0
        return nl + nr

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.sumPaths(root, 0)
    
    def sumNumbers3(self, root: Optional[TreeNode]) -> int:
        tot_sum, cur, depth = 0, 0, 0
        while root:
            print(root.val)
            if root.left:
                pre, depth = root.left, 1
                while pre.right and pre.right != root:
                    pre, depth = pre.right, depth + 1
                # Build connection to top right node closest
                if not pre.right:
                    pre.right = root
                    cur = cur * 10 + root.val
                    root = root.left
                # Root use this to remove connection of pre_node and detect no more left
                else:
                    print(root.val, pre.val, pre.right.val)
                    pre.right = None
                    if not pre.left: tot_sum += cur
                    cur //= 10**depth
                    root = root.right
            else:
                # going back to top right node if you are leaf
                cur = cur * 10 + root.val
                if not root.right: tot_sum += cur
                root = root.right
        return tot_sum

Solution().sumNumbers3(TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0, TreeNode(3), TreeNode(2))))