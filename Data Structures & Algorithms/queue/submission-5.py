class Node:
    def __init__(self, val, prev = None, nxt = None):
        self.val = val
        self.prev = prev
        self.nxt = nxt 

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        return True if self.head is None else False

    def append(self, value: int) -> None:
        node = Node(value, self.tail, None)
        if self.tail:
            self.tail.nxt = node
        self.tail = node
        
        if self.head is None:
            self.head = node

    def appendleft(self, value: int) -> None:
        node = Node(value, None, self.head)
        if self.head: 
            self.head.prev = node
        self.head = node
        
        if self.tail is None:
            self.tail = node

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        value = self.tail.val

        prev = self.tail.prev
        self.tail = prev
        
        if prev: 
            prev.nxt = None
        else:
            self.head = None

        return value


    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        value = self.head.val

        nxt = self.head.nxt
        self.head = nxt

        if nxt:
            nxt.prev = None
        else:
            self.tail = None

        return value
        
