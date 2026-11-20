class ListNode:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(0)
        self.tail = self.head

    def get(self, index: int) -> int:
        current = self.head.next
        i = 0
        while current and i <= index:
            if i == index:
                return current.value
            else:
                current = current.next
                i += 1
        return -1

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val, self.head.next)
        self.head.next = newNode
        if not newNode.next:
            self.tail = newNode

    def insertTail(self, val: int) -> None:
        newTail = ListNode(val, None)
        self.tail.next = newTail
        self.tail = newTail

    def remove(self, index: int) -> bool:
        current = self.head.next
        previous = self.head
        i = 0
        while current and i <= index:
            if i == index:
                previous.next = current.next
                if current == self.tail:
                    self.tail = previous
                return True
            else:
                previous = current
                current = current.next
                i += 1
        return False

    def getValues(self) -> List[int]:
        values = []
        current = self.head.next
        while current:
            values.append(current.value)
            current = current.next
        return values