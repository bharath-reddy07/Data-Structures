from multiprocessing.sharedctypes import Value


class Node:
    def __init__(self,value) -> None:
        self.value=value
        self.next=None
        self.prev=None
class CDLL:
    def __init__(self) -> None:
        self.head=None
        self.tail=None
    def __iter__(self) -> None:
        node=self.head
        while node:
            yield node
            node=node.next
            if node==self.head:
                break
    def creation(self, value):
        node=Node(value)
        node.next=node
        node.prev=node
        self.head=node
        self.tail=node
    def insertion(self,value,location):
        if self.head==None:
            print("Linked list is empty")
        else:
            node=Node(value)
            if location==0:
                node.next=self.head
                node.prev=self.tail
                self.head.prev=node
                self.tail.next=node
                self.head=node
            elif location==-1:
                node.next=self.head
                node.prev=self.tail
                self.tail.next=node
                self.head.prev=node
                self.tail=node
            else:
                tempnode=self.head
                for i in range(0,location-1):
                    tempnode=tempnode.next
                node.next=tempnode.next
                node.prev=tempnode
                tempnode.next.prev=node
                tempnode.next=node
    def traversal(self):
        tempnode=self.head
        while tempnode:
            print(tempnode.value)
            tempnode=tempnode.next
            if tempnode==self.head:
                break
    def reversetraversal(self):
        tempnode=self.tail
        while tempnode:
            print(tempnode.value)
            tempnode=tempnode.prev
            if tempnode==self.tail:
                break
    def deletion(self,location):
        if self.head==self.tail:
            self.head.prev=None
            self.head.next=None
            self.head=None
            self.tail=None
        else:
            if location==0:
                nextnode=self.head.next
                nextnode.prev=self.tail
                self.tail.next=nextnode
                self.head.prev=None
                self.head.next=None
                self.head=nextnode
            elif location==-1:
                previousnode=self.tail.prev
                previousnode.next=self.head
                self.head.prev=previousnode
                self.tail.prev=None
                self.tail.next=None
                self.tail=previousnode
            else:
                tempnode=self.head
                for i in range(0,location-1):
                    tempnode=tempnode.next
                delnode=tempnode.next
                nextnode=delnode.next
                delnode.prev=None
                delnode.next=None
                tempnode.next=nextnode
                nextnode.prev=tempnode
    def deleteentirelist(self):
        tempnode=self.head
        while tempnode:
            tempnode.prev=None
            tempnode=tempnode.next
            if tempnode==self.head:
                break
        self.tail.next=None
        self.head=None
        self.tail=None
circulardoublylinkedlist=CDLL()
circulardoublylinkedlist.creation(1)
circulardoublylinkedlist.insertion(2,0)
circulardoublylinkedlist.insertion(5,-1)
circulardoublylinkedlist.insertion(6,0)
circulardoublylinkedlist.insertion(50,2)
circulardoublylinkedlist.traversal()
circulardoublylinkedlist.reversetraversal()
circulardoublylinkedlist.deletion(3)
circulardoublylinkedlist.deleteentirelist()
print([node.value for node in circulardoublylinkedlist])