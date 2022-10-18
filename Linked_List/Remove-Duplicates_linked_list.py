class Node:
    def __init__(self,value) -> None:
        self.value=value
        self.next=None
class SLL:
    def __init__(self) -> None:
        self.head=None
        self.tail=None
    def __iter__(self) ->None:
        node=self.head
        while node:
            yield node
            node=node.next
    def insertion(self,value):
        node=Node(value)
        if self.head==None:
            self.head=node
            self.tail=node
            node.next=None
        else:
            self.tail.next=node
            node.next=None
            self.tail=node
    def check(self,n):
        i=0
        repeat=[]
        tempnode=self.head
        while True:
            if tempnode.value not in repeat:
                repeat.append(tempnode.value)
                print(repeat)
                i+=1
            else:
                if i==n-1:
                    nodetemp=self.head
                    for j in range(0,n-2):
                        nodetemp=nodetemp.next
                    nodetemp.next=None
                    self.tail=nodetemp
                    n-=1
                    print("deleted last element")
                    break
                else:
                    nodetemp=self.head
                    for j in range(0,i-1):
                        nodetemp=nodetemp.next
                    delnode=nodetemp.next
                    nextnode=delnode.next
                    nodetemp.next=nextnode
                    n-=1
                    print("deleted"+str(i))
            if tempnode==self.tail:
                break
            tempnode=self.head
            for k in range(0,i):
                tempnode=tempnode.next

singlelinkedlist=SLL()
repeat=[]
n=int(input("Enter the number of elements in the linked list:"))
print("Enter the elements of the linked list")
ele=list(map(int,input().split()))
for ele_list in ele:
    singlelinkedlist.insertion(ele_list)
singlelinkedlist.check(n)
print([node.value for node in singlelinkedlist])
