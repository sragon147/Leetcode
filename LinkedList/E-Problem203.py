from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
          head = head.next
    
        curr = head
        prev = None
        
        while curr:
            if curr.val == val:
                prev.next = curr.next
                print(list_to_array(prev))
            else:
                prev = curr
            curr = curr.next
            
        return head
    
    def removeElementsRecursive(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
          return None
        head.next = self.removeElementsRecursive(head.next, val)
        if head.val == val:
          return head.next
        return head

def list_to_array(head):
    array = []
    current = head
    while current:
        array.append(current.val)
        current = current.next
    return array

result = Solution().removeElementsRecursive(ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))), 6) # 1 -> 2 -> 3 -> 4 -> 5
print(list_to_array(result)) # [1, 2, 3, 4, 5]
        