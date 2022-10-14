class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
class SingleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
singlelinkedlist= SingleLinkedList()
node1=Node(5)
node2=Node(7)
singlelinkedlist.head=node1
node1.next=node2
singlelinkedlist.tail=node2
print(node1.next.value)