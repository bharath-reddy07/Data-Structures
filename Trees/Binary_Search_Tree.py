class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        node=self.head
        while not node:
            yield node
            node=node.next

class Queue:
    def __init__(self):
        self.linkedlist=LinkedList()
    def __str__(self):
        values=[str(value) for value in self.linkedlist]
        return " ".join(values)
    def enqueue(self,value):
        node=Node(value)
        if self.linkedlist.head is None:
            self.linkedlist.head=node
            self.linkedlist.tail=node
        self.linkedlist.tail.next=node
        self.linkedlist.tail=node
    
    def isEmpty(self):
        if self.linkedlist.head==None:
            return True
        return False

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        node=self.linkedlist.head
        if self.linkedlist.head==self.linkedlist.tail:
            self.linkedlist.head=None
            self.linkedlist.tail=None
        self.linkedlist.head=self.linkedlist.head.next
        return node

class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftnode=None
        self.rightnode=None

def insertNode(rootNode,node_value):
    if rootNode.data==None:
         rootNode.data=node_value
    elif node_value<=rootNode.data:
        if rootNode.leftnode is None:
            rootNode.leftnode=TreeNode(node_value)
        else:
            insertNode(rootNode.leftnode,node_value)
    else:
        if rootNode.rightnode is None:
            rootNode.rightnode=TreeNode(node_value)
        else:
            insertNode(rootNode.rightnode,node_value)

def preOrderTraversal(rootNode):
    if rootNode is None or rootNode.data is None:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftnode)
    preOrderTraversal(rootNode.rightnode)

def search(rootNode,search_value):
    if rootNode is None:
        print("Item not found")
    elif rootNode.data==search_value:
        print("Successful") 
    elif search_value<rootNode.data:
        search(rootNode.leftnode,search_value)
    else:
        search(rootNode.rightnode,search_value)

def minValue(rootNode):
    current=rootNode
    while(current.leftnode):
        current=current.leftnode
    return current

def delete(rootNode,del_value):
    if rootNode.data==del_value:
        if rootNode.leftnode==None and rootNode.rightnode==None:
            rootNode=None
            return rootNode
        elif rootNode.leftnode is not None and rootNode.rightnode is None:
            temp=rootNode.leftnode
            rootNode=None
            return temp
        elif rootNode.rightnode is not None and rootNode.leftnode is None:
            temp=rootNode.rightnode
            rootNode=None
            return temp
        else:
            temp=minValue(rootNode.rightnode)
            rootNode.data=temp.data
            rootNode.rightnode=delete(rootNode.rightnode,temp.data)
    elif rootNode.data>del_value:
        rootNode.leftnode=delete(rootNode.leftnode,del_value)
    else:
        rootNode.rightnode=delete(rootNode.rightnode,del_value)
    return rootNode  
        
BST=TreeNode(None)
insertNode(BST,70)
insertNode(BST,50)
insertNode(BST,90)
insertNode(BST,30)
insertNode(BST,60)
insertNode(BST,80)
insertNode(BST,100)
insertNode(BST,20)
insertNode(BST,40)
insertNode(BST,10)
delete(BST,20)
preOrderTraversal(BST)

