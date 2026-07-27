# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        groupPrev = dummy

        while True:

            kth = groupPrev

            for _ in range(k):
                kth = kth.next

                if not kth:
                    return dummy.next

            groupNext = kth.next

            prev = groupNext
            current = groupPrev.next

            while current != groupNext:

                nextNode = current.next

                current.next = prev

                prev = current

                current = nextNode

            temp = groupPrev.next

            groupPrev.next = kth

            groupPrev = temp
        