from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        n = len(nums) // 2
        tree = TreeNode()
        current = tree
        current.val = nums[n]
        print(nums[:n], len(nums), nums)
        current.left = self.sortedArrayToBST(nums[:n])
        current.right = self.sortedArrayToBST(nums[n+1:])
        return tree

def print_tree(node):
    if node is not None:
        print(node.val)
        print_tree(node.left)
        print_tree(node.right)

result = Solution().sortedArrayToBST([-10, -3, 0, 5, 9])
print_tree(result)