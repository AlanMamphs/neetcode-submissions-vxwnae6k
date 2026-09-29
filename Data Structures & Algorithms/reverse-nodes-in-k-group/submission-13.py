# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def kth(self, l, k):
        for _ in range(k):
            l = l.next
            if not l:
                return None
        return l

    def reverse(self, start, end):
        prev = end
        curr = start

        while curr != end:
           curr.next, prev, curr = prev, curr, curr.next

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        root = ListNode(0, head)
        group_prev = root
        
        while True:
            kth = self.kth(group_prev, k)
            if not kth:
                break
            group_next = kth.next
            group_start = group_prev.next
            
            self.reverse(group_start, group_next)
            
            group_prev.next = kth
            group_prev = group_start

        return root.next
        



