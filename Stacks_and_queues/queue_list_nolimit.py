class queue:
    def __init__(self) -> None:
        self.list=[]
    def print_values(self):
        print(self.list)
    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            return False
    def enqueue(self,value):
        self.list.append(value)
        return "Element added to queue"
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.list.pop(0)
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.list[0]
    def delete(self):
        self.list=[]
stack=queue()
stack.print_values()
print(stack.isEmpty())
print(stack.enqueue(1))
print(stack.enqueue(2))
print(stack.enqueue(3))
print(stack.enqueue(4))
print(stack.enqueue(5))
print(stack.isEmpty())
stack.print_values()
print(stack.dequeue())
print(stack.dequeue())
print(stack.peek())
stack.print_values()
stack.delete()
stack.print_values()
print(stack.dequeue())