# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        curr = dummy
        while l1 or l2 or carry:
            l1_val = l1 and l1.val or 0
            l2_val = l2 and l2.val or 0

            _sum = carry + l1_val + l2_val
            carry = _sum // 10
            curr.next = ListNode(_sum % 10)
            curr = curr.next
            l1 = l1 and l1.next
            l2 = l2 and l2.next

        return dummy.next        