# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:   
        newHead = head
        if head and head.next:
            following = head.next
            newHead = self.reverseList(following)
            following.next = head
        if head:
            head.next = None

        return newHead