from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
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

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
          print(root)
          return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
          return root
        return l or r

Solution().lowestCommonAncestor(array_to_tree([3,5,1,6,2,0,8,None,None,7,4]), array_to_tree([5]), array_to_tree([1])) # 3
