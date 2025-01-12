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
            # next 2 -> 3 -> 4 -> 5
            next = curr.next
            # curr.next -> None -> 1 -> 2 -> 3 ->4
            curr.next = prev
            # prev -> 1 -> 2 -> 3 -> 4 -> 5
            # prev.next = cur.next -> None -> 1 -> 2 -> 3 -> 4
            prev = curr
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
