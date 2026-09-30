# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def kth(self, l, k):
        for _ in range(k):
            l = l and l.next
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
            end = self.kth(group_prev, k)
            if not end:
                break
            start = group_prev.next
            group_start_next = end.next
            
            self.reverse(start, group_start_next)
            group_prev.next = end
            group_prev = start
        return root.next
