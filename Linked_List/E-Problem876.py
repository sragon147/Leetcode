class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        slow = fast = head
        while fast is not None and fast.next is not None:
            slow = head.next
            fast = head.next.next
        return slow
