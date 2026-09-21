# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, l):
        curr = l
        prev = None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev
    def kth(self, l, k):
        while k and l:
            l = l.next
            k -= 1
        return l

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        root = ListNode(0)
        curr = root
        next_kth = head
        
        while next_kth:
            end = self.kth(next_kth, k - 1)
            if not end:
                break
            tmp = end.next
            end.next = None
            curr.next = self.reverse(next_kth)
            curr = next_kth
            next_kth = tmp
        
        curr.next = next_kth

        return root.next