from typing import Optional

class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
          return None
        
        pointerA = headA
        pointerB = headB
        while pointerA != pointerB:
          pointerA = pointerA.next if pointerA else headB
          pointerB = pointerB.next if pointerB else headA
            
        return pointerA