class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.pointer = TreeNode()
        prev = TreeNode()

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
                    
                    prev.right = root
                    prev = prev.right
                    
                    root.left = None
                    root = root.right
            else:
                if not self.pointer.right:
                    self.pointer.right = root
                
                prev.right = root
                prev = prev.right

                root = root.right

    def next(self) -> int:
        self.pointer = self.pointer.right
        return self.pointer.val

    def hasNext(self) -> bool:
        return self.pointer.right is not None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root_node=root
        self.current_node=root
        self.stack=[]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.current_node is not None or len(self.stack)!=0

    def next(self):
        """
        :rtype: int
        """
        while self.current_node:
            self.stack.append(self.current_node)
            self.current_node=self.current_node.left
        next=self.stack.pop()
        self.current_node=next.right
        return next.val

class BSTIterator:
    def __init__(self, root: TreeNode):
        self.root = root

    def next(self) -> int:
        while self.root:
            if not self.root.left: 
                break
            pre = self.root.left
            while pre.right:
                pre = pre.right
            pre.right = self.root
            pre = self.root.left
            self.root.left = None
            self.root = pre
        value = self.root.val
        self.root = self.root.right
        return value

    def hasNext(self) -> bool:
        return self.root