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
        
        if k <= 1:
            return head
        while left:
            count = 0
            right = left
            while right.next and count < k:
                right = right.next
                count += 1
            
            if count == k:
                temp = right.next
                right.next = None
                left.next, left = self.reverse(left.next)
                left.next = temp
            else:
                break
        return root.next


        















