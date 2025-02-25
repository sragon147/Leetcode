class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def dfs(tree):
            nonlocal max_sum
            
            if not tree:
                return 0
            
            left = dfs(tree.left)
            right = dfs(tree.right)
            
            max_sum = max(max_sum, tree.val + left + right, tree.val, tree.val + left, tree.val + right)
            
            return max(tree.val + left, tree.val + right, tree.val)

        dfs(root)

        return max_sum

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float('-inf')
        def dfs(node):
            nonlocal max_path
            if not node:
                return 0
            leftmax = max(dfs(node.left), 0)
            rightmax = max(dfs(node.right), 0)
            curr = node.val + leftmax + rightmax
            max_path = max(curr, max_path)
            
            return node.val + max(leftmax, rightmax)
        dfs(root)
        return max_path