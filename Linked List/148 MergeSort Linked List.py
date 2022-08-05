from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time complexity O(nlogn), space complexity O(logn). Merge sort.
        def mergeSort(headPoint: Optional[ListNode], length: int) -> Optional[ListNode]:
            if length == 0:
                return None
            if length == 1:
                headPoint.next = None
                return headPoint
            ptr = headPoint
            mid = int(length / 2)
            for i in range(mid):
                ptr = ptr.next
            midPoint = ptr
            leftList = mergeSort(headPoint, mid)
            rightList = mergeSort(midPoint, length - mid)
            return merge(leftList, rightList)

        def merge(left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
            resHead = ListNode()
            pMerge = resHead
            while left and right:
                if left.val <= right.val:
                    pMerge.next = left
                    pMerge = left
                    left = left.next
                else:
                    pMerge.next = right
                    pMerge = right
                    right = right.next
            pMerge.next = left if left else right
            return resHead.next

        p = head
        size = 0
        while p:
            size += 1
            p = p.next
        return mergeSort(head, size)


if __name__ == '__main__':
    print(1)
