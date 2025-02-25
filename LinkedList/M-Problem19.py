from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def printList(self, head):
        while head:
            print(head.val, end=" ")
            head = head.next
        print()
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        begin = dummy
        for _ in range(n):
            head = head.next
        while head:
            head = head.next
            begin = begin.next
        begin.next = begin.next.next
        return dummy.next

Solution().removeNthFromEnd(ListNode(1), 1)