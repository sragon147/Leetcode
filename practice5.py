class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, l1, l2):
        dummyHead = ListNode(0)
        current = dummyHead
        current.next = ListNode(value)
        current = current.next
