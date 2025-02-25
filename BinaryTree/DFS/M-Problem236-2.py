from typing import Optional

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
        res = None
        def dfs(tree: 'TreeNode'):
            nonlocal res
            if tree is None:
                return False
            
            print(tree.val)
            left = dfs(tree.left)
            right = dfs(tree.right)
            
            if tree.val == p.val or tree.val == q.val:
                if left or right:
                    res = tree
                    return False
                return True

            if left and right:
                res = tree
                return False
            
            return left or right
        dfs(root)
        return res
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.dfs(root, p, q)
        return self.lcs
    
    def dfs(self, root, p, q):
        if not root:
            return False

        current_node_p_or_q = root == p or root == q
        left_has_p_or_q = self.dfs(root.left, p, q)
        right_has_p_or_q = self.dfs(root.right, p, q)

        if current_node_p_or_q + left_has_p_or_q + right_has_p_or_q == 2:
            self.lcs = root
        
        return current_node_p_or_q or left_has_p_or_q or right_has_p_or_q

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def getAncestors(root, node, path):
            if root == None:
                return None

            path.append(root)
            if root.val == node.val:
                return path

            left = getAncestors(root.left, node, path)
            if left != None:
                return left

            right = getAncestors(root.right, node, path)
            if right != None:
                return right
            
            path.pop()


        ancestors1 = getAncestors(root, p, [])
        ancestors2 = getAncestors(root, q, [])
        i = 0
        size = min(len(ancestors1), len(ancestors2))
        while i < size and ancestors1[i].val == ancestors2[i].val:
            i += 1
        return ancestors1[i-1]
    
    def lowestCommonAncestor(self, root, p, q):
        def path(root, goal):
            path, stack = [], [root]
            while True:
                node = stack.pop()
                if node:
                    if node not in path[-1:]:
                        path += node,
                        if node == goal:
                            return path
                        stack += node, node.right, node.left
                    else:
                        path.pop()
        return next(a for a, b in zip(path(root, p), path(root, q))[::-1] if a == b)

    def lowestCommonAncestor(self, root, p, q):
        if root in (None, p, q): return root
        left, right = (self.lowestCommonAncestor(kid, p, q)
                    for kid in (root.left, root.right))
        return root if left and right else left or right

Solution().lowestCommonAncestor(
    TreeNode(3, 
        TreeNode(5, 
            TreeNode(6), 
            TreeNode(2, TreeNode(7), TreeNode(4))
        ), 
        TreeNode(1, TreeNode(0), TreeNode(8))
    ), 
    TreeNode(1), 
    TreeNode(5)
)