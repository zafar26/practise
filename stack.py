class Stack:
    
    def __init__(self):
        self.stack = []

    def add(self, dataval):
# Use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
# Use peek to look at the top of the stack

    def peek(self,value):     
	    return self.stack[-value]

AStack = Stack()
val = input()
AStack.add(val)
AStack.add("Tue")
AStack.peek(1)
AStack.peek(2)

print(AStack.peek(1))
print(AStack.peek(2))

AStack.add("Wed")
AStack.add("Thu")
print(AStack.peek(1))
print(AStack.peek(2))
