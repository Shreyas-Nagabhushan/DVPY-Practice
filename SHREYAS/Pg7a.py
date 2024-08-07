class Stack:
    def __init__(self):
        self.container = []
    def push(self, item):
        self.container.append(item)
    def pop(self):
        if len(self.container) == 0:
            return -1
        return self.container.pop()
    def is_empty(self):
        return len(self.container) == 0 
    def peek(self):
        if self.is_empty():
            return -1
        return self.container[-1]

class Queue:
    def __init__(self):
        self.container = []
    def push(self, item):
        self.container.insert(0, item)
    def pop(self):
        if len(self.container) == 0:
            return -1
        return self.container.pop(0)
    def is_empty(self):
        return len(self.container) == 0 
    def peek(self):
        if self.is_empty():
            return -1
        return self.container[0]
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # Output: 3
print(stack.peek())  # Output: 2
print(stack.is_empty())  # Output: False

# Queue example
queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)
print(queue.pop())  # Output: 1
print(queue.peek())  # Output: 2
print(queue.is_empty())  # Output: False