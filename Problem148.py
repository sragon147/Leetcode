from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.count = 0
        
    def dfs(self, root: TreeNode, X: int) -> None:
        if root is None:
            return
        if root.val >= X:
            X = root.val
            self.count += 1
        self.dfs(root.left, X)
        self.dfs(root.right, X)
    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(root, float('-inf'))
        return self.count
    
def array_to_tree(array):
    if not array:
        return None

    root = TreeNode(array[0])
    queue = deque([root])
    i = 1

    while queue:
        current = queue.popleft()
        
        if i < len(array) and array[i] is not None:
            current.left = TreeNode(array[i])
            queue.append(current.left)
        i += 1
        
        if i < len(array) and array[i] is not None:
            current.right = TreeNode(array[i])
            queue.append(current.right)
        i += 1

    return root

result = Solution().goodNodes(array_to_tree([-1,5,-2,4,4,2,-2,None,None,-4,None,-2,3,None,-2,0,None,-1,None,-3,None,-4,-3,3,None,None,None,None,None,None,None,3,-3])) # 4
print(result) # 4