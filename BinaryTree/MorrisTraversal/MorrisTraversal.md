# Morris Inorder Traversal (Left-Root-Right)
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def morris_inorder(root):
    curr = root
    while curr:
        if curr.left is None:
            print(curr.val, end=" ")  # Process node
            curr = curr.right
        else:
            predecessor = curr.left
            while predecessor.right and predecessor.right != curr:
                predecessor = predecessor.right

            if predecessor.right is None:
                predecessor.right = curr  # Create temporary link
                curr = curr.left
            else:
                predecessor.right = None  # Remove link
                print(curr.val, end=" ")  # Process node
                curr = curr.right

# Example Usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

morris_inorder(root)
```

## Output:
```bash
4 2 5 1 3
```

# Morris Inorder Traversal (Root-Left-Right)
```python
def morris_preorder(root):
    curr = root
    while curr:
        if curr.left is None:
            print(curr.val, end=" ")  # Process node
            curr = curr.right
        else:
            predecessor = curr.left
            while predecessor.right and predecessor.right != curr:
                predecessor = predecessor.right

            if predecessor.right is None:
                print(curr.val, end=" ")  # Process node
                predecessor.right = curr  # Create temporary link
                curr = curr.left
            else:
                predecessor.right = None  # Remove link
                curr = curr.right

# Example Usage
morris_preorder(root)
```

## Output:
```bash
1 2 4 5 3
```