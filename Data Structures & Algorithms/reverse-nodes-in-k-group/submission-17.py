# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, start, end):
        prev = end
        curr = start

        while curr != end:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
    
    def kth(self, head, k):
        for _ in range(k):
            head = head and head.next
        return head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        root = ListNode(0, head)
        prev_end = root

        while True:
            kth = self.kth(prev_end, k)
            if not kth:
                break
            
            next_start = kth.next
            curr_start = prev_end.next
            
            self.reverse(curr_start, next_start)

            prev_end.next = kth

            prev_end = curr_start
        
        return root.next
