class Node:
    def __init__(self,value) -> None:
        self.value=value
        self.next=None
class SLL:
    def __init__(self) -> None:
        self.head=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            print(node.value)
            node=node.next
class Stack:
    def __init__(self) -> None:
        self.linkedlist=SLL()
    def print_values(self):
        node=self.linkedlist.head
        while node:
            print(node.value)
            node=node.next
    def isEmpty(self):
        if self.linkedlist.head==None:
            return True
        else:
            return False
    def push(self,value):
        node=Node(value)
        if self.isEmpty():
            self.linkedlist.head=node
        else:
            node.next=self.linkedlist.head
            self.linkedlist.head=node
        return "Element added to stack"
    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        else:
            popped_ele=self.linkedlist.head.value
            self.linkedlist.head=self.linkedlist.head.next
            return popped_ele
    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        else:
            return self.linkedlist.head.value
    def delete(self):
        self.linkedlist.head=None
stack=Stack()
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