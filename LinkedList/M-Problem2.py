class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        res = ListNode(0)
        head = res
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            sum_val = l1_val + l2_val + carry
            carry = sum_val // 10
            head.next = ListNode(sum_val % 10)
            res = res.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            head.next = ListNode(carry)
        return res.next