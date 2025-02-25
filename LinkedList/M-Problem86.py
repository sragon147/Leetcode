class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        larger_or_equal = ListNode()
        smaller = ListNode()
        larger_or_equal_curr = larger_or_equal
        smaller_curr = smaller

        while head:
            if head.val < x:
                smaller_curr.next = head
                smaller_curr = smaller_curr.next
            else:
                larger_or_equal_curr.next = head
                larger_or_equal_curr = larger_or_equal_curr.next
            
            head = head.next

        larger_or_equal_curr.next = None
        smaller_curr.next = larger_or_equal.next
        return smaller.next