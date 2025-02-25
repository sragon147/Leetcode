class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        prev = None
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
                    if prev is not None and prev >= root.val:
                        return False
                    prev = root.val
                    root = root.right
            else:
                if prev is not None and prev >= root.val:
                    return False
                prev = root.val
                root = root.right
        return True