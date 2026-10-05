# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        root = ListNode()
        curr = root
        carry = 0

        while l1 or l2 or carry:
            left = l1 and l1.val or 0
            right = l2 and l2.val or 0
            total = left + right + carry
            curr.next = ListNode()
            curr = curr.next
            curr.val = total % 10
            carry = total // 10
            l1 = l1 and l1.next
            l2 = l2 and l2.next
        return root.next
