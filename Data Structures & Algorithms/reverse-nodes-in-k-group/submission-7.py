# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def print(self, head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        print(arr)
        
    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        head, tail = prev, head
        return head, tail
    
    def kth(self, head, k):
        while head and k > 0:
            head = head.next
            k -= 1
        return head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        root = left = ListNode(0, head)
        
        while left:
            kth = self.kth(left, k)

            if kth:
                tmp = kth.next
                kth.next = None
                left.next, left = self.reverse(left.next)
                left.next = tmp
            else:
                break
        return root.next
