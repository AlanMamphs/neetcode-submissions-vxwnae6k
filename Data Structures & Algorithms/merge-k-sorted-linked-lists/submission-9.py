# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
        def mergeTwoLists(self, l1, l2):
            root = ListNode()
            curr = root
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
            
            while len(lists) > 1:
                merged_lists = []
                for i in range(0, len(lists), 2):
                    l1 = lists[i]
                    if i + 1 < len(lists):
                        l2 = lists[i + 1]
                    else:
                        l2 = None
                    
                    merged_lists.append(self.mergeTwoLists(l1, l2))
                lists = merged_lists
            
            return lists and lists[0] or None