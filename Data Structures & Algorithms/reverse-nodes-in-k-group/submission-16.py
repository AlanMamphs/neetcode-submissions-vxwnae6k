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
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        root = ListNode(0, head)
        prev_end = root

        while True:
            start = prev_end.next
            end = self.kth(prev_end, k)
            if not end:
                break
            next_start = end.next
            self.reverse(start, next_start)

            prev_end.next = end
            prev_end = start
        return root.next


