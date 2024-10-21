from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def print_list(self, head: Optional[ListNode]) -> None:
        array = []
        while head:
            array.append(head.val)
            head = head.next
        print(array)
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        rev = self.reverse_list(slow)
        slow = head
        sum = 0
        while rev:
            sum = max(sum , slow.val + rev.val)
            rev = rev.next
            slow = slow.next
        return sum
    def pairSumShort(self, head: Optional[ListNode]) -> int:
        prev, slow, fast = None, head, head
        while fast and fast.next:
            fast = fast.next.next
            slow.next, prev, slow = prev, slow, slow.next
        ans = 0
        while prev:
            ans = max(ans, prev.val + slow.val)
            prev, slow = prev.next, slow.next
        return ans

result = Solution().pairSum(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))) # [3, 4, 5], [5, 4, 3]
print(result) # 9