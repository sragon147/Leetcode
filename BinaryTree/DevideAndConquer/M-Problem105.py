from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        post = 0
        in_map = {}

        def build(l, r):
            nonlocal post
            if l > r: return None

            val = preorder[post]
            node = TreeNode(val)
            post += 1

            node.left = build(l, in_map[val] - 1)
            node.right = build(in_map[val] + 1, r)
            
            return node

        for i, val in enumerate(inorder):
            in_map[val] = i

        return build(0, len(preorder) - 1)
    
    def buildTree3(self, preorder, inorder):
        # stop is use to detect when there is no more node on the left side of stop node
        # due to behavior of inorder, the left side of a node will present on the left of inorder array
        # right node of curr node will still be on the left side of parent of curr node
        def build(stop):
            print(stop, inorder, preorder)
            if inorder and inorder[-1] != stop:
                root = TreeNode(preorder.pop())
                root.left = build(root.val)
                inorder.pop()
                root.right = build(stop)
                return root
        preorder.reverse()
        inorder.reverse()
        return build(None)

Solution().buildTree3([4, 2, 3, 6, 5, 7], [3, 2,  4, 5, 6, 7])