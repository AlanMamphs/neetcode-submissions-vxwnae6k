# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        root = ListNode(0, head)
        offset = root.next
        for _ in range(n):
            offset = offset.next
        
        curr = root

        while offset:
            curr = curr.next
            offset = offset.next
        

        curr.next = curr.next.next
        return root.next
