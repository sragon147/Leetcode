from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            ind = inorder.index(postorder.pop())
            print(postorder)
            root = TreeNode(inorder[ind])
            root.right = self.buildTree(inorder[ind+1:], postorder)
            root.left = self.buildTree(inorder[0:ind], postorder)
            return root
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        post = len(postorder) - 1
        in_map = {}

        def build(l, r):
            nonlocal post
            if l > r: return None

            val = postorder[post]
            node = TreeNode(val)
            post -= 1

            node.right = build(in_map[val] + 1, r)
            node.left = build(l, in_map[val] - 1)
            
            return node

        for i, val in enumerate(inorder):
            in_map[val] = i

        return build(0, len(postorder) - 1)
    
    def buildTree3(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # same idea as 105, stop is use to detect when there is no more node on the right side of stop node
        # because if right side exist it will block the stop node, making inorder[-1] != stop True.
        def build(stop):
            if inorder and inorder[-1] != stop:
                root = TreeNode(postorder.pop())
                root.right = build(root.val)
                inorder.pop()
                root.left = build(stop)
                return root
        return build(None)
        
Solution().buildTree3([9,3,15,20,7], [9,15,7,20,3])