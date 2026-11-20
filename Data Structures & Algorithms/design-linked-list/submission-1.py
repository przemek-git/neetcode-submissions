class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        # dummy node, self.head.next is real head
        self.head = ListNode(-1)

    def get(self, index: int) -> int:
        cur = self.head.next
        for _ in range(index):
            if not cur:
                return -1
            cur = cur.next
        return cur.val if cur else -1

    def addAtHead(self, val: int) -> None:
        self.head.next = ListNode(val, self.head.next)

    def addAtTail(self, val: int) -> None:
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = ListNode(val)

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.head
        for _ in range(index):
            if not cur.next:
                return
            cur = cur.next 
        newNode = ListNode(val, cur.next)
        cur.next = newNode

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head
        for _ in range(index):
            if not cur.next:
                return
            cur = cur.next
        if cur.next: 
            cur.next = cur.next.next 

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)