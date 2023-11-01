from typing import Optional, List
from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = ListNode(-1)
        prev.next = head
        toDel = prev
        p = head
        while n > 0:
            p = p.next
            n -= 1
        while p:
            p = p.next
            toDel = toDel.next
        toDel.next = toDel.next.next
        return prev.next


if __name__ == '__main__':
    res = Solution().removeNthFromEnd(["lc", "cl", "gg"])
    print(res)
