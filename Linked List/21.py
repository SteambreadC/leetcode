from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists_wrong(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2, pre = list1, list2, list1

        if (p1.val < p2.val):
            start = p1
        else:
            start = p2

        while p1 and p2:
            if p1.val <= p2.val:
                pre = p1
                p1 = p1.next
                pre.next = p2
                pre = p2

            elif p1.val > p2.val:
                pre = p2
                p2 = p2.next
                pre.next = p1
                pre = p1

        if p1 != None:
            pre.next = p1
        else:
            pre.next = p2
        return start

    def mergeTwoLists2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2, start = list1, list2, ListNode(-1, None)
        pre=start

        while p1 and p2:
            if p1.val <= p2.val:
                pre.next = p1
                p1 = p1.next
            elif p1.val > p2.val:
                pre.next = p2
                p2 = p2.next
            pre=pre.next
        if p1!=None:
            pre.next=p1
        else:
            pre.next=p2

        return start.next



if __name__ == '__main__':
    sol = Solution()
    print(sol.isSubsequence("abc", "ahdgdc"))
