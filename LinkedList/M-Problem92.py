from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right: return head
        p = dummy = ListNode(None)
        dummy.next = head
        for _ in range(left-1): p = p.next
        tail = p.next

        for _ in range(right-left):
            tmp = p.next # 2
            p.next = tail.next # 1 -> 3
            tail.next = tail.next.next # 3 -> 4
            p.next.next = tmp 
        return dummy.next

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right: return head
        pre = dummy = ListNode(None)
        dummy.next = head
        for _ in range(left-1): pre = pre.next
        curr = pre.next

        for _ in range(right-left):
            forw = curr.next # 2
            curr.next = forw.next
            forw.next = pre.next
            pre.next = forw
        return dummy.next
Solution().reverseBetween(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, 4)