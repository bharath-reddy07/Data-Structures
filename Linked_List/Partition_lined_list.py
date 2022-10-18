class Node:
    def __init__(self,value) -> None:
        self.value=value
        self.next=None
class SLL:
    def __init__(self) -> None:
        self.head=None
        self.tail=None
    def __iter__(self)-> None:
        node=self.head
        while node:
            yield node
            node=node.next
    def insertion(self,value,key):
        node=Node(value)
        if self.head==None:
            self.head=node
            self.tail=node
        else:
            if value>=key:
                self.tail.next=node
                self.tail=node
            else:
                node.next=self.head
                self.head=node
singlelinkedlist=SLL()
print("Enter the elements of the linked list")
listele=list(map(int,input().split()))
key=int(input("Enter the value about which u want to partition the linked list:"))
for ele in listele:
    singlelinkedlist.insertion(ele,key)
print([node.value for node in singlelinkedlist])