# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # [1,2,3,4,5]

        print(head)

        # [5]
        if head and head.next is None:
            return head

        # [4, 5]
        if head and head.next:
            incoming = head.next
            reversed_head = self.reverseList(incoming)
            incoming.next = head         
            head.next = None
            return reversed_head
        # []
