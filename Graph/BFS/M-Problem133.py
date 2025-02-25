from typing import Optional
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: 
            return None

        node_dict = {}
        stack = [node]
        while stack:
            cur = stack.pop()
            if cur not in node_dict:
                node_dict[cur] = Node(cur.val)
            for neighbor in cur.neighbors:
                if neighbor not in node_dict:
                    stack.append(neighbor)

        for key, value in node_dict.items():
            for neighbor in key.neighbors:
                value.neighbors.append(node_dict[neighbor])

        return node_dict[node]
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        
        q, clones = deque([node]), {node.val: Node(node.val, [])}
        while q:
            cur = q.popleft() 
            cur_clone = clones[cur.val]            

            for ngbr in cur.neighbors:
                if ngbr.val not in clones:
                    clones[ngbr.val] = Node(ngbr.val, [])
                    q.append(ngbr)
                    
                cur_clone.neighbors.append(clones[ngbr.val])
                
        return clones[node.val]

    def cloneGraph(self, node: 'Node') -> 'Node':
        old_to_new = {}
        
        def clone(node):
            if node in old_to_new:
                return old_to_new[node]
            
            copy = Node(node.val)
            old_to_new[node] = copy
            
            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))
            return copy 
        
        return clone(node) if node else None