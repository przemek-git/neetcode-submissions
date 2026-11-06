# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        nxt = list1
        while nxt:
            vals.append(nxt.val)
            nxt = nxt.next
        nxt = list2
        while nxt:
            vals.append(nxt.val)
            nxt = nxt.next        
        vals.sort()
        if not vals:
            return None
        fake_first = ListNode()
        current = fake_first
        for val in vals:
            lst = ListNode(val, None)
            current.next = lst
            current = lst
        return fake_first.next