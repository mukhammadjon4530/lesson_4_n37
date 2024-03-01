from random import randint

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Error: Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Error: Stack is empty")

    def size(self):
        return len(self.items)

# Example usage:
stack = Stack()
data = []
for i in range(25):
    random_number = randint(100, 200)
    data.append(random_number)
    stack.push(random_number)
print(f"Queue {data}")
print(f"Stack {stack.items}")


