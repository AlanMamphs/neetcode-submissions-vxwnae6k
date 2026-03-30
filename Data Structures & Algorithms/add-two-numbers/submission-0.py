# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        prev = 0

        while l1 or l2:
            left = l1 and l1.val or 0
            right = l2 and l2.val or 0
            sum_of_digits = left + right + prev
            prev, curr = sum_of_digits // 10, sum_of_digits % 10

            node.next = ListNode(curr)
            node = node.next
            l1 = l1 and l1.next
            l2 = l2 and l2.next
        if prev:
            node.next = ListNode(prev)
        return dummy.next
