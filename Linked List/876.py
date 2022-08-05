from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid = p = head
        while p and p.next:
            mid = mid.next
            p = p.next.next
        return mid
