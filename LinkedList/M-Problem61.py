from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        curr = head
        len_head = 1
        while curr.next:
            curr = curr.next
            len_head += 1
        curr.next = head

        k = k % len_head

        curr = head
        for _ in range (len_head - k - 1):
            curr = curr.next
        
        head = curr.next
        curr.next = None
        return head

Solution().rotateRight(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)

