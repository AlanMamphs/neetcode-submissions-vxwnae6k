# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        root = ListNode()
        curr = root
        while l1 or l2:
            curr.next = ListNode()
            curr = curr.next

            val1 = l1 and l1.val or 0
            val2 = l2 and l2.val or 0

            val = (carry + val1 + val2)
            curr.val = val % 10
            carry = val // 10
            l1 = l1 and l1.next
            l2 = l2 and l2.next
        if carry:
            curr.next = ListNode(carry)
        return root.next
