class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        if len(self.stack) == 0:
            return 'stack is Empty'
        return self.stack.pop()
        
    def peek(self):
        if len(self.stack) == 0:
            return 'stack is Empty'
        return self.stack[-1]
        
    def printStack(self):
        return self.stack
        
s = Stack()
s.push(4)
s.push(2)
s.push(7)
print(s.printStack())
print(s.pop())
print(s.peek())
s.push(10)
s.push(20)
print(s.printStack())


output:
[4, 2, 7]
7
2
[4, 2, 10, 20]

=== Code Execution Successful ===



