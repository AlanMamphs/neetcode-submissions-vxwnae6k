# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev, head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        root = left = ListNode(0, head)
        right = head
        if k <= 1:
            return head
        while left:
            count = 1
            while right and count < k:
                right = right.next
                if right:
                    count += 1
            if count == k:
                if right:
                    temp = right.next
                    right.next = None
                    right = temp
                left.next, left = self.reverse(left.next)
                left.next = right
            else:
                break
        return root.next


        















