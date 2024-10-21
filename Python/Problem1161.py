from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])

        max_levels = levels = 1
        max_sum = root.val

        while queue: 
            curr_sum = 0
            level_size=len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                curr_sum += node.val
                
                if node.left:
                    queue.append(node.left) 
                if node.right:
                    queue.append(node.right)
            
            if curr_sum > max_sum:
                max_sum, max_levels = curr_sum, levels
            levels += 1

        return max_levels
Solution().maxLevelSum(TreeNode(1, TreeNode(7, TreeNode(7), TreeNode(-8)), TreeNode(2))) # 2