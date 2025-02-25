import heapq

class MinStack:

    def __init__(self):
        self.stk = []
        self.mstk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if len(self.mstk) == 0:
            self.mstk.append(val)
        elif val < self.mstk[-1]:
            self.mstk.append(val)
        else:
            self.mstk.append(self.mstk[-1])

    def pop(self) -> None:
        self.stk.pop()
        self.mstk.pop()
        
    def top(self) -> int:
        return self.stk[-1]
        
    def getMin(self) -> int:
        return self.mstk[-1]

class Node:
    def __init__(self, val, min, next):
        self.val = val
        self.min = min
        self.next = next

class MinStack:
    def __init__(self):
        self.head = None
    
    def push(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val, val, None)
        else:
            self.head = Node(val, min(val, self.head.min), self.head)
    
    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val
    
    def getMin(self) -> int:
        return self.head.min
        