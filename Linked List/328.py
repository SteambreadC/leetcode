from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        po=head
        pe=head.next
        head_even=pe
        while po and pe:
            if not pe.next:
                break
            po.next=pe.next
            po=po.next
            pe.next=po.next
            pe=pe.next
        po.next=head_even
        return head