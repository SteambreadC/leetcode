from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ptr = head
        size = 0
        while ptr:
            size += 1
            ptr = ptr.next
        ptr = head
        if size < 2:
            return True

        for i in range(int(size / 2)):
            ptr = ptr.next
        mid = ptr

        prev = mid
        ptr = mid.next
        prev.next = None
        while ptr:
            pnext = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = pnext
        ptr = head

        while ptr and prev:
            if ptr.val != prev.val:
                return False
            ptr = ptr.next
            prev = prev.next

        return True


if __name__ == '__main__':
    print(1)
