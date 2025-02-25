class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge_sort(head):
            if not head or not head.next:
                return head
            
            slow, fast = head, head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            
            mid = slow.next
            slow.next = None

            left = merge_sort(head)
            right = merge_sort(mid)

            return merge(left, right)

        def merge(left, right):
            dummy = ListNode()
            prev = dummy
            while left and right:
                if left.val < right.val:
                    prev.next = left
                    left = left.next
                else:
                    prev.next = right
                    right = right.next
                prev = prev.next
            
            prev.next = left if left else right   
            return dummy.next
        
        return merge_sort(head)

