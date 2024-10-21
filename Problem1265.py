class ImmutableListNode:
    def __init__(self, value):
        self.value = value
    def printValue(self): # print the value of this node.
        pass
    def getNext(self): # return the next node.
        return None

def printLinkedListInReverse(head: 'ImmutableListNode') -> None:
    stack = []
    current = head
    # Traverse the list and push the nodes onto the stack
    while current is not None:
        stack.append(current)
        current = current.getNext()
    # Pop from the stack and print the values
    while stack:
        node = stack.pop()
        node.printValue()