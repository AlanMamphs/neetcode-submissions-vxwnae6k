# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        root = ListNode()
        res = root
        while curr1 and curr2:
            if curr1.val < curr2.val:
                temp = curr1
                root.next = curr1
                curr1 = curr1.next
                root = temp
            else:
                temp = curr2
                root.next = curr2
                curr2 = curr2.next
                root = temp
        root.next = curr1 or curr2
        
        return res.next