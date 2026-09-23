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
        curr = slow
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        first = head
        second = prev
        curr = ListNode()
        while first and second:
            curr.next = first
            curr = curr.next
            first = first.next
            curr.next = second
            curr = curr.next
            second = second.next

        curr.next = None