from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.num_paths = 0
        # prefix sums keeps track of how many times a sum has appeared in the tree in the traversal
        # if the difference curr_sum - targetsum = prefix_sum, then that means that path should be added to num_paths
        self.prefix_sums = {}
        self.prefix_sums[0] = 1
        def dfs(root, curr_sum, targetSum):
            if root == None:
                return
            curr_sum += root.val
            print(curr_sum)
            # returns the value of prefix_sums[curr_sum - targetSum] if the key exists. otherwise returns 0
            self.num_paths += self.prefix_sums.get(curr_sum - targetSum, 0)
            print(self.prefix_sums, self.num_paths)
                
            if curr_sum in self.prefix_sums.keys():
                self.prefix_sums[curr_sum] += 1
            else:
                self.prefix_sums[curr_sum] = 1

            dfs(root.left, curr_sum, targetSum)
            dfs(root.right, curr_sum, targetSum)

            # once both dfs() returns, this node will no longer be in the path, so you should remove it from the dict
            self.prefix_sums[curr_sum] -= 1

        dfs(root, 0, targetSum)
        return self.num_paths

Solution().pathSum(TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))), TreeNode(-3, None, TreeNode(11))), 8) # 3