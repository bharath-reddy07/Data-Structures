"""You hae two numbers represented by a linked list , where each node contains a single digit.The digits are stored in reverse order,
Write a function that adds the two numbers and returns the sum as a linked list

Example:
list1= 7->1->6    list2=5->9->2
sum is 617+295=912
Therefore Sumlist=2->1->9
"""
import math
class Node:
    def __init__(self,value) -> None:
        self.value=value
        self.next=None
class num1:
    def __init__(self) -> None:
        self.head=None
        self.tail=None
    def __iter__(self)-> None:
        node=self.head
        while node:
            yield node
            node=node.next
    def insertion(self,value)-> None:
        node=Node(value)
        if self.head==None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
    def access(self)-> int:
        tempnode=self.head
        sum=0
        i=0
        while tempnode:
            sum+=tempnode.value*(10**i)
            tempnode=tempnode.next
            i+=1
        return sum
    
class num2:
    def __init__(self) -> None:
        self.head=None
        self.tail=None
    def __iter__(self)-> None:
        node=self.head
        while node:
            yield node
            node=node.next
    def insertion(self,value)-> None:
        node=Node(value)
        if self.head==None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
    def access(self)-> int:
        tempnode=self.head
        sum=0
        i=0
        while tempnode:
            sum+=tempnode.value*(10**i)
            tempnode=tempnode.next
            i+=1
        return sum
class sumlist:
    def __init__(self) -> None:
        self.head=None
        self.tail=None
    def __iter__(self)-> None:
        node=self.head
        while node:
            yield node
            node=node.next
    def insertion(self,value)-> None:
        node=Node(value)
        if self.head==None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
numfirst=num1()
numsecond=num2()
ans=sumlist()
firstno=int(input("Enter the 1st no"))
secondno=int(input("Enter the second no"))
while firstno>0:
    rem=firstno%10
    firstno=int(firstno/10)
    numfirst.insertion(rem)
#print([node.value for node in numfirst])
while secondno>0:
    rem=secondno%10
    secondno=int(secondno/10)
    numsecond.insertion(rem)
#print([node.value for node in numsecond])
Num1=numfirst.access()
Num2=numsecond.access()
#print(Num1)
#print(Num2)
sum=Num1+Num2
while sum>0:
    rem=sum%10
    sum=int(sum/10)
    ans.insertion(rem)
print([node.value for node in ans])