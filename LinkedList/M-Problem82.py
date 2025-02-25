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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        start = dummy
        count = 0
        while head:
            while head.next and head.val == head.next.val:
                head = head.next
                count += 1
            if count == 0:
                print(head.val)
                start.next = head
                start = start.next 
            count = 0
            head = head.next
        start.next = None
        return dummy.next

Solution().deleteDuplicates(ListNode(1, ListNode(2, ListNode(2))))