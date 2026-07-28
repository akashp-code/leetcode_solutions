# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow

        while curr:
            newno = curr.next
            curr.next = prev
            prev = curr
            curr = newno

        fst = head
        sec = prev

        while sec:
            if fst.val != sec.val:
                return False

            fst = fst.next
            sec = sec.next

        return True

        

        