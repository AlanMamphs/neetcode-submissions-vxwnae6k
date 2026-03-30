# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def print(self, head):
        curr = head
        array = []
        while curr:
            array.append(curr.val)
            curr = curr.next
        print(array)
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = ListNode(0, head)

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        root = curr = ListNode(0)
        left = head
        right = prev
        self.print(left)
        self.print(right)
        while left and right:
            curr.next = left
            left = left.next
            curr = curr.next
            curr.next = right
            right = right.next
            curr = curr.next
        
        curr.next = left or right

        
            
