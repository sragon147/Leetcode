from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        q = deque()
        q.append(root)

        while q:
            q.append(None)
            while True:
                node = q.popleft()
                if not node:
                    break
                node.next = q[0]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return root
                
    def connect2(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        q = deque([root])
        while q:
            sz = len(q)
            pre = None
            for _ in range(sz):
                cur = q.popleft()
                if pre is not None:
                    pre.next = cur
                pre = cur
                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
        return root
    def connect3(self, root):
        tail = dummy = TreeLinkNode(0)
        while root:
            tail.next = root.left
            if tail.next:
                tail = tail.next
            tail.next = root.right
            if tail.next:
                tail = tail.next
            # tail dummy -> left -> right
            # root left has next from 2nd recursive, so it move to node right
            root = root.next
            if not root:
                # reset tail to dummy
                tail = dummy
                # root become most left
                root = dummy.next
