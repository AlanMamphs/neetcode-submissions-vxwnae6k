# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def kth(self, l, k):
        curr = l
        while k > 0 and curr:
           curr = curr.next
           k -= 1

        if k == 0:
            return curr

    def reverse(self, l):
        prev = None
        curr = l

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        root = ListNode(0, head)
        curr = root
        
        while curr:
            kth = self.kth(curr, k)
            if not kth:
                break
            head = kth.next
            kth.next = None
            tmp = curr.next
            curr.next = self.reverse(curr.next)
            tmp.next = head
            curr = tmp

        return root.next
        



