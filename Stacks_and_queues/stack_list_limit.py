


class Stack:
    def __init__(self,max_value) -> None:
        self.list=[]
        self.max_value=max_value
    def print_values(self):
        print(self.list)
    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            return False
    def isFull(self):
        if len(self.list)==self.max_value:
            return True
        else:
            return False
    def push(self,value):
        if self.isFull():
            return "Stack is full"
        else:
            self.list.append(value)
            return "Element added"
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.list.pop()
    def peek(self):
        return self.list[len(self.list)-1]
    def delete(self):
        self.list=[]
stack=Stack(4)
stack.print_values()
print(stack.isEmpty())
print(stack.push(1))
print(stack.push(2))
print(stack.push(3))
print(stack.push(4))
print(stack.push(5))
print(stack.isEmpty())
stack.print_values()
print(stack.pop())
print(stack.pop())
print(stack.peek())
stack.print_values()
stack.delete()
stack.print_values()
print(stack.pop())