# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next
        slow.next = None

        prev, curr = None, second_half

        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        first_half = head
        second_half = prev

        while second_half:
            tmp = first_half.next
            tmp2 = second_half.next
            first_half.next = second_half 
            second_half.next = tmp
            first_half = tmp
            second_half = tmp2