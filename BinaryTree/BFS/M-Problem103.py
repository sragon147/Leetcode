class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = defaultdict(deque)
        def traversal(root, level):
            if root:
                if level % 2 == 0:
                    res[level].append(root.val)
                else:
                    res[level].appendleft(root.val)
                traversal(root.left, level+1)
                traversal(root.right, level+1)
        traversal(root, 0)
        return [list(d) for d in res.values()]
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = deque([root])
        direction = True
        while queue:
            level = deque()
            for i in range(len(queue)):
                node = queue.popleft()
                if direction:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(list(level))
            direction = not direction
        return result