class Stack:
    stack: list = []

    def __init__(self):
        pass

    def push(self, el):
        self.stack.append(el)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[- 1]

    def is_empty(self):
        return not self.stack
