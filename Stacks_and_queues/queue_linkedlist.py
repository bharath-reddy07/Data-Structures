class Node:
    def __init__(self,value) -> None:
        self.value=value
        self.next=None
class SLL:
    def __init__(self) -> None:
        self.head=None
        self.tail=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            print(node.value)
            node=node.next
class queue:
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
    def enqueue(self,value):
        node=Node(value)
        if self.isEmpty():
            self.linkedlist.head=node
            self.linkedlist.tail=node
        else:
            self.linkedlist.tail.next=node
            self.linkedlist.tail=node
        return "Element added to the queue"
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            node=self.linkedlist.head
            value=node.value
            if self.linkedlist.head==self.linkedlist.tail:
                self.linkedlist.head=None
                self.linkedlist.tail=None
            else:
                self.linkedlist.head=node.next
            return value
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.linkedlist.head.value
    def delete(self):
        self.linkedlist.head=None
        self.linkedlist.tail=None
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