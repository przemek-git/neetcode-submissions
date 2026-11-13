# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(previous, current):
            if current is None:
                return previous 
            else:
                following = current.next 
                current.next = previous
                return reverse(current, following)
        return reverse(None, head)
        