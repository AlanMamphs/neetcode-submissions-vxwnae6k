# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev, head
    
    def kth(self, head, k):
        curr = head
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        root = left = ListNode(0, head)
        
        while left:
            kth = self.kth(left, k)
            if kth:
                temp = kth.next
                kth.next = None
                left.next, left = self.reverse(left.next)
                left.next = temp
            else:
                break
        return root.next


        















