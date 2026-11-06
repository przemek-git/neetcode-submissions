# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        traversed = []
        current = head
        while current and current.next:
            if current.val in traversed:
                return True
            traversed.append(current.val)
            current = current.next
        return False