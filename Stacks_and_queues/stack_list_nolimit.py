class Stack:
    def __init__(self):
        self.list=[]
    def print_stack(self):
        print(self.list)
    def push(self,value):
        self.list.append(value)
        return("Value added")
    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            return False
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.list.pop()
    def peek(self):
        return self.list[len(self.list)-1]
    def delete(self):
        self.list=[]
stack=Stack()
stack.print_stack()
print(stack.isEmpty())
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.isEmpty())
stack.print_stack()
print(stack.pop())
print(stack.pop())
print(stack.peek())
stack.print_stack()
stack.delete()
stack.print_stack()
print(stack.pop())


