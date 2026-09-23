# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        root = ListNode(0, head)
        curr = root
        
        while n:
            curr = curr.next
            n -=1

        nth = root
        prev = None
        
        while curr:
            prev = nth
            nth = nth.next
            curr = curr.next
        
        prev.next = nth.next
        nth.next = None

        return root.next