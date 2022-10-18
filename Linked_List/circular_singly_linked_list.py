class Node:
    def __init__(self,value=None) -> None:
        self.value=value
        self.next=None
class CSLL:
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
            
    def creation(self,value):
        node1=Node(value)
        self.head=node1
        self.tail=node1
        node1.next=node1
    def insertion(self,value,location):
        node=Node(value)
        if self.head==None:
            node.next=node
            self.head=node
            self.tail=node
        elif location==0:
            node.next=self.head
            self.head=node
            self.tail.next=node
        elif location==-1:
            self.tail.next=node
            self.tail=node
            self.tail.next=self.head
        else:
            tempnode=self.head
            for i in range(0,location-1):
                tempnode=tempnode.next
            node.next=tempnode.next
            tempnode.next=node
    def traversal(self):
        node=self.head
        while node:
            print(node.value)
            node=node.next
            if node==self.head:
                break
    def deletion(self,location):
        if self.head==self.tail:
            self.head.next=None
            self.head=None
            self.tail=None
        elif location==0:
            self.head=self.head.next
            self.tail.next=self.head
        elif location==-1:
            tempnode=self.head
            while tempnode:
                tempnode=tempnode.next
                if tempnode.next==self.tail:
                    break
            tempnode.next=self.head
            self.tail=tempnode
        else:
            tempnode=self.head
            for i in range(0,location-1):
                tempnode=tempnode.next
            nextnode=tempnode.next
            tempnode.next=nextnode.next
    def deleteentirelist(self):
        self.tail.next=None
        self.head=None
        self.tail=None

            
    
circularsinglylinkedlist=CSLL()
circularsinglylinkedlist.creation(1)
circularsinglylinkedlist.insertion(2,0)
circularsinglylinkedlist.insertion(5,-1)
circularsinglylinkedlist.insertion(6,0)
circularsinglylinkedlist.insertion(50,2)
circularsinglylinkedlist.traversal()
circularsinglylinkedlist.deletion(2)
circularsinglylinkedlist.deleteentirelist()
print([node.value for node in circularsinglylinkedlist])