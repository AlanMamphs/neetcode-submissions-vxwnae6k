# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cache = []
        curr = head
        while curr:
            cache.append(curr)
            curr = curr.next
            cache[-1].next = None
        
        l = 0
        r = len(cache) - 1

        while l < r:
            cache[l].next = cache[r]
            if l + 1 != r:
                cache[r].next = cache[l + 1]
            l += 1
            r -= 1



            