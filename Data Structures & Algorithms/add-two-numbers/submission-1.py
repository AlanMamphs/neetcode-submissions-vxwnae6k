# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = curr = ListNode()

        carry = 0
        while l1 or l2 or carry:
            left = l1 and l1.val or 0
            right = l2 and l2.val or 0
            l1 = l1 and l1.next
            l2 = l2 and l2.next
            _sum = carry + left + right
            carry = _sum // 10
            node = ListNode(_sum % 10)
            curr.next = node
            curr = curr.next
        return root.next