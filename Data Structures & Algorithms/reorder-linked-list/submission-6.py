# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        slow.next = None
        start1 = head
        start2 = prev


        root = curr = ListNode()

        while start1 and start2:
            curr.next = start1
            curr = curr.next
            start1 = start1.next

            curr.next = start2
            curr = curr.next
            start2 = start2.next
        
        curr.next = start1 or start2
