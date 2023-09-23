import numpy as np

class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.front = -1
        self.back = -1
        self.size = 0
        self.array = np.zeros(self.capacity, dtype=object)

    def empty(self):
        return self.size == 0

    def get_size(self) -> int:
        return self.size

    def push_front(self, data):
        if self.size == self.capacity:
            raise IndexError("Deque is full")

        new_node = Node(data)
        if self.empty():
            self.front = self.back = 0
        else:
            self.front = (self.front - 1) % self.capacity
        self.array[self.front] = new_node
        self.size += 1

    def push(self, data):
        if self.size == self.capacity:
            raise IndexError("Deque is full")

        new_node = Node(data)
        if self.empty():
            self.front = self.back = 0
        else:
            self.back = (self.back + 1) % self.capacity
        self.array[self.back] = new_node
        self.size += 1
    
    def pop_front(self) -> int:
        if self.empty():
            raise IndexError("Deque is empty")

        data = self.array[self.front].item
        if self.size == 1:
            self.front = self.back = -1
        else:
            self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return data
    
    def pop(self) -> int:
        if self.empty():
            raise IndexError("Deque is empty")

        data = self.array[self.back].item
        if self.size == 1:
            self.front = self.back = -1
        else:
            self.back = (self.back - 1) % self.capacity
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

    def resize(self):
        new_capacity = self.capacity * 2
        new_array = np.zeros(new_capacity, dtype=object)
        if not self.empty():
            i = 0
            current_index = self.front
            while current_index != -1:
                new_array[i] = self.array[current_index]
                current_index = (current_index + 1) % self.capacity
                i += 1
        self.front = 0
        self.back = self.size - 1
        self.capacity = new_capacity
        self.array = new_array

def isPalindrome(s: str) -> bool:
    # Initialize a Deque using the Deque class.
    deque = Deque()
    while not deque.empty():
        if deque.pop_front() != deque.pop():
            return False
    return True

test1 = "racecar"
test2 = "hello"
print(isPalindrome(test1))  # True
print(isPalindrome(test2))  # False

