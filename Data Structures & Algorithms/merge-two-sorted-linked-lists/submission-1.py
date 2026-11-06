# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        fake_first = ListNode()
        current = fake_first

        while list1 or list2:
            if list1 and list2 and list1.val > list2.val:
                current.next = ListNode(list2.val, None)
                current = current.next
                list2 = list2.next
            elif list1 and list2:
                current.next = ListNode(list1.val, None)
                current = current.next
                list1 = list1.next
            elif list1:
                current.next = ListNode(list1.val, None)
                current = current.next
                list1 = list1.next
            else:
                current.next = ListNode(list2.val, None)
                current = current.next
                list2 = list2.next  

        return fake_first.next
        
        
        # brute force solution:
        # vals = []
        # nxt = list1
        # while nxt:
        #     vals.append(nxt.val)
        #     nxt = nxt.next
        # nxt = list2
        # while nxt:
        #     vals.append(nxt.val)
        #     nxt = nxt.next        
        # vals.sort()
        # if not vals:
        #     return None
        # fake_first = ListNode()
        # current = fake_first
        # for val in vals:
        #     lst = ListNode(val, None)
        #     current.next = lst
        #     current = lst
        # return fake_first.next