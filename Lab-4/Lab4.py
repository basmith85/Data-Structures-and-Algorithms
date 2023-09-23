class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self,):
        self.front = None
        self.back = None
        self.size = 0

    def empty(self):
        if self.back == None and self.front == None:
            return True
        else:
            return False
            
    def get_size(self) -> int:
         return self.size
    
    def push_front(self, data):
        new_node = Node(data)
        if self.empty():
            self.front = self.back = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        self.size += 1

    def push(self, data):
        new_node = Node(data)
        if self.empty():
            self.front = self.back = new_node
        else:
            self.back.next = new_node
            new_node.prev = self.back
            self.back = new_node
        self.size += 1
    
    def pop_front(self) -> int:
        if self.empty():
            raise IndexError("Deque is empty")
        data = self.front.item
        if self.size == 1:
            self.front = self.back = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.size -= 1
        return data
    
    def pop(self) -> int:
        if self.empty():
            raise IndexError("Deque is empty")
        data = self.back.item
        if self.size == 1:
            self.front = self.back = None
        else:
            self.back = self.back.prev
            self.back.next = None
        self.size -= 1
        return data
    
    def front(self) -> int:
        if self.empty():
            raise IndexError("Deque is empty")
        return self.front.item
    
    def back(self) -> int:
        if self.empty():
            raise IndexError("Deque is empty")
        return self.back.item
    
def reverse_deque(deque):
    reversed_deque = Deque()
    while not deque.empty():
        reversed_deque.push_front(deque.pop_front())

    return reversed_deque

deque = Deque()
deque.push(1)
deque.push(2)
deque.push(3)

reversed_deque = reverse_deque(deque)
while not reversed_deque.empty():
    print(reversed_deque.pop_front())  # Should output 3, 2, 1.