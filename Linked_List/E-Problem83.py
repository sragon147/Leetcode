from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        stack = [head.val]
        current = head

        while current.next:
            if current.next.val in stack:
                current.next = current.next.next
            else:
                stack.append(current.next.val)
                current = current.next
        
        return head

result = Solution().deleteDuplicates(ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3))))))
while result:
    print(result.val, end=" -> ")
    result = result.next
