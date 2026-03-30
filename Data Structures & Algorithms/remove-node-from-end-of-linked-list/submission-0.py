# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        curr = head
        while curr:
            arr.append(curr)
            curr = curr.next
        k = len(arr) - n
        curr = head
        dummy = node = ListNode()

        for i, v in enumerate(arr):
            if i == k:
                node.next = None
                continue
            node.next = v
            node = node.next
    
        return dummy.next