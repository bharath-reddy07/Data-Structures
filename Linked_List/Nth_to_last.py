class Node:
    def __init__(self,value) -> None:
        self.value=value
        self.next=None
class SLL:
    def __init__(self) -> None:
        self.head=None
        self.tail=None
    def __iter__(self) -> None:
        node=self.head
        while node:
            yield node
    def insertion(self,value):
        node=Node(value)
        if self.head==None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
    def access(self,location,n):
        i=(n-location)
        tempnode=self.head
        for j in range (0,i):
            tempnode=tempnode.next
        print(tempnode.value)
singlelinkedlist=SLL()
print("Enter the elements of the linked list")
linkedlistele=list(map(int,input().split()))
length=len(linkedlistele)
for ele in linkedlistele:
    singlelinkedlist.insertion(ele)
location=int(input("Enter the location of the element from the end whose value u want to access:"))
singlelinkedlist.access(location,length)
