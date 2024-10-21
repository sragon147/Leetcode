from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            next = curr.next
            # Make the next node become previous node 
            # curr.next -> None -> 1 -> 2 -> 3 ->4
            curr.next = prev
            # Make previous node become current node, which on next interation will become next node 
            # prev -> 1 -> 2 -> 3 -> 4 -> 5
            prev = curr
            # Take the rest of the list 
            # curr -> 2 -> 3 -> 4 -> 5
            curr = next
        return prev

def list_to_array(head):
    array = []
    current = head
    while current:
        array.append(current.val)
        current = current.next
    return array

result = Solution().reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))) # 5 -> 4 -> 3 -> 2 -> 1
