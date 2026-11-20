class Node:
    def __init__(self, value, nxt = None):
        self.value = value
        self.nxt = nxt

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head.nxt

    def isEmpty(self) -> bool:
        return not self.head.nxt

    def append(self, value: int) -> None:
        node = Node(value)
        if self.tail:
            self.tail.nxt = node
            self.tail = node
        else: 
            self.head.nxt = node
            self.tail = self.head.nxt

    def appendleft(self, value: int) -> None:
        node = Node(value, self.head.nxt)
        self.head.nxt = node
        if not self.tail:
            self.tail = node

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        if self.head.nxt == self.tail:
            value = self.head.nxt.value
            self.head.nxt = self.tail = None
            return value

        cur = self.head.nxt
        while cur.nxt != self.tail:
            cur = cur.nxt
        
        value = self.tail.value
        cur.nxt = None
        self.tail = cur

        return value


    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        value = self.head.nxt.value
        self.head.nxt = self.head.nxt.nxt
        if not self.head.nxt:
            self.tail = self.head.nxt
        return value
