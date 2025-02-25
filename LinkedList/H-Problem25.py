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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(begin, end):
            curr = begin
            prev = end.next
            while prev != end:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev, begin
        if k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while head:
            end = prev
            for _ in range(k):
                end = end.next
                if not end:
                    return dummy.next
            next_begin = end.next
            head, next_prev = reverse(head, end)
            prev.next = head
            prev = next_prev
            head = next_begin
            
        return dummy.next

Solution().reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)