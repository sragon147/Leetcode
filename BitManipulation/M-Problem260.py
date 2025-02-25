from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        count = []
        self.helper(root, count)
        return count[k-1]
        
    def helper(self, node, count):
        if not node:
            return
        
        self.helper(node.left, count)
        count.append(node.val)
        self.helper(node.right, count)
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = -1
        self.helper(root, k, res)
        return res
        
    def helper(self, node, count, res):
        if not node:
            return
        
        self.helper(node.left, count, res)
        count -= 1
        if count == 0:
            res = node.val
            return
        self.helper(node.right, count, res)
    
    def kthSmallest3(self, root, k):
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
            
    def kthSmallest3(self, root, k):
        while root:
            if root.left:
                pre = root.left
                while pre.right and pre.right != root:
                    pre = pre.right
                if not pre.right:
                    pre.right = root
                    root = root.left
                else:
                    pre.right = None
                    k -= 1
                    if k == 0:
                        return root.val
                    root = root.right
            else:
                k -= 1
                if k == 0:
                    return root.val
                root = root.right
        return -1
class TTreeNode:
    def __init__(self, x):
        self.val = x
        self.count = 1
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.tRoot = None

    def kthSmallest(self, root, k):
        self.tRoot = self.buildTTree(root)
        return self.helper(self.tRoot, k)

    def helper(self, tRoot, k):
        left_count = 0 if not tRoot.left else tRoot.left.count
        if k == left_count + 1:
            return tRoot.val
        elif k > left_count + 1:
            return self.helper(tRoot.right, k - left_count - 1)
        else:
            return self.helper(tRoot.left, k)

    def buildTTree(self, root):
        if not root:
            return None
        tNode = TTreeNode(root.val)
        tNode.left = self.buildTTree(root.left)
        tNode.right = self.buildTTree(root.right)
        tNode.count += (0 if not tNode.left else tNode.left.count)
        tNode.count += (0 if not tNode.right else tNode.right.count)
        return tNode

Solution().kthSmallest3(TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6)), 3)