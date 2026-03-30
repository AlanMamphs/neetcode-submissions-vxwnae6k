# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        root = curr = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return root.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = lists and lists[0] or None

        for i in range(1, len(lists)):
            root = self.mergeTwoLists(root, lists[i])
        

        return root