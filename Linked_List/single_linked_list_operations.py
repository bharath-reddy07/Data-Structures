class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
class SingleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    def insertion(self,value,location):
        newNode=Node(value)
        if self.head==None:
            self.head=newNode
            self.tail=newNode
        else:
            if location==0:
                newNode.next=self.head
                self.head=newNode
            elif location==-1:
                self.tail.next=newNode
                self.tail=newNode
            else:
                currentNode=self.head
                for i in range(0,location-1):
                    currentNode=currentNode.next
                nextNode=currentNode.next
                currentNode.next=newNode
                newNode.next=nextNode
    def search(self,key):
        if self.head==None:
            print("Linkedlist is empty")
        else:
            currentNode=self.head
            while currentNode is not self.tail:
                if currentNode.value==key:
                    return "Element Present"
                currentNode=currentNode.next
            return "Element does not exist"
    def delete(self,location):
        if self.head==None:
            print("Linkedlist is empty")
        else:
            if location==0:
                self.head=self.head.next
            elif location==-1:
                currentNode=self.head
                while currentNode.next is not self.tail:
                    currentNode=currentNode.next
                currentNode.next=self.tail
            else:
                currentNode=self.head
                for i in range(0,location-1):
                    currentNode=currentNode.next
                nextNode=currentNode.next
                currentNode.next=nextNode.next
singlelinkedlist= SingleLinkedList()
singlelinkedlist.insertion(2,0)
singlelinkedlist.insertion(22,0)
singlelinkedlist.insertion(25,-1)
singlelinkedlist.insertion(28,2)
print([node.value for node in singlelinkedlist])
print(singlelinkedlist.search(30))
singlelinkedlist.delete(2)
print([node.value for node in singlelinkedlist])