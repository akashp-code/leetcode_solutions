# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head

        beforeLeft = dummy

        for _ in range(left - 1):
            beforeLeft = beforeLeft.next

        leftNode = beforeLeft.next

        prev = None
        current = leftNode

        for _ in range(right - left + 1):

            next_node = current.next

            current.next = prev

            prev = current

            current = next_node

        beforeLeft.next = prev

        leftNode.next = current

        return dummy.next