from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is not None and head.next is not None:
            p = head.next
            prev = head
            head.next = None
        else:
            return head
        while p:
            pn = p.next
            p.next = prev
            prev = p
            p = pn
        return prev
