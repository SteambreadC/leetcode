from typing import Optional, List

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr=head
        length=0
        while ptr:
            length+=1
            ptr=ptr.next
        res=ListNode()
        res.next=head
        ptr=res
        for i in range(length-n):
            ptr=ptr.next
        ptr.next=ptr.next.next
        return res.next


    def sol2_2pointers(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''Java code
        public
        ListNode
        removeNthFromEnd(ListNode
        head, int
        n) {
            ListNode
        dummy = new
        ListNode(0);
        dummy.next = head;
        ListNode
        first = dummy;
        ListNode
        second = dummy;
        // Advances
        first
        pointer
        so
        that
        the
        gap
        between
        first and second is n
        nodes
        apart
        for (int i = 1; i <= n + 1; i++) {
            first = first.next;
        }
        // Move first to the end, maintaining the gap
        while (first != null) {
        first = first.next;
        second = second.next;
        }
        second.next = second.next.next;
        return dummy.next;
        }
        '''
