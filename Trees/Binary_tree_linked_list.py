class Node:
    def __init__(self,value=None):
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
        while node:
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
        if(self.linkedlist.head==None):
            self.linkedlist.head=node
            self.linkedlist.tail=node
        else:
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
        else:
            self.linkedlist.head=self.linkedlist.head.next
        return node

class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftnode=None
        self.rightnode=None
BT=TreeNode("Drinks")
hot=TreeNode("Hot")
cold=TreeNode("Cold")
BT.leftnode=hot
BT.rightnode=cold
tea=TreeNode("Tea")
coffee=TreeNode("Coffee")
cocacola=TreeNode("CocaCola")
fanta=TreeNode("Fanta")
hot.leftnode=tea
hot.rightnode=coffee
cold.leftnode=cocacola
cold.rightnode=fanta

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftnode)
    preOrderTraversal(rootNode.rightnode)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftnode)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightnode)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftnode)
    postOrderTraversal(rootNode.rightnode)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    queue=Queue()
    queue.enqueue(rootNode)
    while not(queue.isEmpty()):
        root=queue.dequeue()
        print(root.value.data)
        if(root.value.leftnode is not None):
            queue.enqueue(root.value.leftnode)
        if(root.value.rightnode is not None):
            queue.enqueue(root.value.rightnode)

def searchBT(rootNode,search):
    if not rootNode:
        return
    queue=Queue()
    queue.enqueue(rootNode)
    while not(queue.isEmpty()):
        root=queue.dequeue()
        if(search == root.value.data):
            return "Item Found"
        if(root.value.leftnode is not None):
            queue.enqueue(root.value.leftnode)
        if(root.value.rightnode is not None):
            queue.enqueue(root.value.rightnode)
    return "Item not found"

def insertBT(rootNode,ele_value):
    if not rootNode:
        rootNode=ele_value
        return "Successfully Inserted"
    queue=Queue()
    queue.enqueue(rootNode)
    while not(queue.isEmpty()):
        root=queue.dequeue()
        if(root.value.leftnode is not None):
            queue.enqueue(root.value.leftnode)
        else:
            root.value.leftnode=ele_value
            return "Successfully Inserted"
        if(root.value.rightnode is not None):
            queue.enqueue(root.value.rightnode)
        else:
            root.value.rightnode=ele_value
            return "Successfully Inserted"

def getDeepestNode(rootNode):
    if not rootNode:
        return
    queue=Queue()
    queue.enqueue(rootNode)
    while not(queue.isEmpty()):
        root=queue.dequeue()
        if(root.value.leftnode is not None):
            queue.enqueue(root.value.leftnode)
        if(root.value.rightnode is not None):
            queue.enqueue(root.value.rightnode)
    deepestnode=root.value
    return deepestnode

def delNode(rootNode,del_value):
    if not rootNode:
        return
    queue=Queue()
    queue.enqueue(rootNode)
    while not(queue.isEmpty()):
        root=queue.dequeue()
        if(root.value.data==del_value):
            dnode=getDeepestNode(rootNode)
            root.value.data=dnode.data
            dnode.data=None
            return "Node deleted Successfully"
        if(root.value.leftnode is not None):
            queue.enqueue(root.value.leftnode)
        if(root.value.rightnode is not None):
            queue.enqueue(root.value.rightnode)

print(searchBT(BT,"Hot"))