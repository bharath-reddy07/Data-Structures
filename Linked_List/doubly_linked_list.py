class Node:
    def __init__(self,value=None) -> None:
        self.value=value
        self.next=None
        self.prev=None
class DLL:
    def __init__(self) -> None:
        self.head=None
        self.tail=None
    def __iter__(self) -> None:
        node=self.head
        while node:
            yield node
            node=node.next
            if node==None:
                break
    def creation(self,value):
        node=Node(value)
        node.next=None
        node.prev=None
        self.head=node
        self.tail=node
    def insertion(self,value,location):
        node=Node(value)
        if self.head==None:
            print("Create a node")
        elif location==0:
            nextnode=self.head
            node.next=nextnode
            self.head=node
            node.prev=None
            nextnode.prev=node
        elif location==-1:
            previousnode=self.tail
            node.next=None
            node.prev=previousnode
            previousnode.next=node
            self.tail=node
        else:
            tempnode=self.head
            for i in range(0,location-1):
                tempnode=tempnode.next
            nextnode=tempnode.next
            node.next=nextnode
            node.prev=tempnode
            nextnode.prev=node
            tempnode.next=node
    def traversal(self):
        if self.head==None:
            print("Linked list has 0 elements")
        else:
            tempnode=self.head
            while tempnode:
                print(tempnode.value)
                tempnode=tempnode.next
                if tempnode==None:
                    break
    def reversetraversal(self):
        if self.head==None:
            print("The Linked list does not have any elements")
        else:
            tempnode=self.tail
            while tempnode:
                print(tempnode.value)
                tempnode=tempnode.prev
                if tempnode==None:
                    break
    def deletion(self,location):
        if self.head==self.tail:
            self.head=None
            self.tail=None
        else:
            if location==0:
                tempnode=self.head
                nextnode=tempnode.next
                tempnode.next=None
                self.head=nextnode
                nextnode.prev=None
            elif location==-1:
                tempnode=self.tail
                previousnode=tempnode.prev
                tempnode.prev=None
                previousnode.next=None
                self.tail=previousnode
            else:
                tempnode=self.head
                for i in range(0,location-1):
                    tempnode=tempnode.next
                delnode=tempnode.next
                nextnode=delnode.next
                delnode.next=None
                delnode.prev=None
                tempnode.next=nextnode
                nextnode.prev=tempnode
    def deleteentirelist(self):
        tempnode=self.head
        while tempnode:
            tempnode.prev=None
            tempnode=tempnode.next
            if tempnode==None:
                break
        self.head=None
        self.tail=None
doublylinkedlist=DLL()
doublylinkedlist.creation(1)
doublylinkedlist.insertion(2,0)
doublylinkedlist.insertion(5,-1)
doublylinkedlist.insertion(6,0)
doublylinkedlist.insertion(50,2)
doublylinkedlist.traversal()
doublylinkedlist.reversetraversal()
doublylinkedlist.deletion(-1)
doublylinkedlist.deleteentirelist()
print([node.value for node in doublylinkedlist])