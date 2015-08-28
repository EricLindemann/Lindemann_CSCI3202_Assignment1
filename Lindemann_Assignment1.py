#Eric Lindemann CSCI3202 HW1

import Queue

#queue allows for adding numbers one at a time and removing all at once
def addQueue(q,item):
    q.put(item)

def deQueue(q):
    while not q.empty():
        print q.get()
     
#LIFO stack allows for push, pop and checksize
class myStack:
    def __init__(self):
        self.items = []
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def checkSize(self):
        return len(self.items)

#unordered binary tree allows for add, delete and print
class myBinaryTree:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def add(self,value,parentValue):
        if self.data == parentValue:
            if self.left == None:
                self.left = myBinaryTree(value)
            elif self.right == None:
                self.right = myBinaryTree(value)
            else:
                print "Parent has two nodes, node not added"
        else:
            if self.left != None:
                self.left.add(value,parentValue)
            if self.right !=None:
                self.right.add(value,parentValue)
            if self.left and self.right == None:
                print "Parent not found"

    def delete(self,value):
        if self.left != None:
            if self.left.data == value:
                if self.left.left or self.left.right != None:
                    print "Node not deleted, has children"
                else:
                    self.left = None;
            else:
                self.left.delete(value)
       
        if self.right != None:
            if self.right.data == value:
                if self.right.left or self.right.right != None:
                    print "Node not deleted, has children"
                else:
                    self.right = None;
            else:
                self.right.delete(value)

    def printTree(self):
        print self.data
        if self.left != None:
            self.left.printTree()
        if self.right != None:
            self.right.printTree()


class Graph:
    def __init__(self):
        self.dict = {}

    def addVertex(self,value):
        if self.dict.has_key(value):        
            print "Vertex already exists"
        else:
            self.dict[value] = None

    def addEdge(self,value1,value2):
        if self.dict.has_key(value1) and self.dict.has_key(value2):
            if self.dict[value1] == None:
                self.dict[value1] = [value2]
            else:
                self.dict[value1].append(value2)
            if self.dict[value2] == None:
                self.dict[value2] = [value1]
            else:
                self.dict[value2].append(value1)
        else:
            print "One or more vertices not found."

    def findVertex(self,value):
        if self.dict.has_key(value):
            print "%d has adjacent vertices %s" % (value, str(self.dict[value]).strip('[]'))
        else:
            print "Vertex does not exist"




#tests
#Queue should add numbers and deQueue in FIFO order
print "Queue"
newQueue = Queue.Queue()
print "Adding numbers to new Queue in order 1,2,...10"
for i in range (1,11):
    addQueue(newQueue,i)
print "Calling deQueue"
deQueue(newQueue)

#Stack should add numbers and pop off in LIFO order
print "\nStack"
print "Adding numbers to stack in order 1,2,...10"
newStack = myStack()
for i in range (1,11):
    newStack.push(i)
print "Calling pop on stack until empty"
while newStack.checkSize() != 0:
    print newStack.pop()

print "\nBinary Tree"
#should add numbers to proper nodes and delete numbers if they have no children
print "Making tree with values 1,2,...11"
BT = myBinaryTree(1)
BT.add(2,1)
BT.add(3,1)
BT.add(4,2)
BT.add(5,2)
BT.add(6,3)
BT.add(7,3)
BT.add(8,4)
BT.add(9,4)
BT.add(10,5)
BT.add(11,5)
BT.printTree()
print "deleting 11 and 8 from tree"
BT.delete(11)
BT.delete(8)
BT.printTree()

print "\nGraph"
print "Making graph"
newGraph = Graph()
print "Adding vertices 1,2,...10"
for i in range (1,11):
    newGraph.addVertex(i)
print"Adding 20 edges"
newGraph.addEdge(2,4)
newGraph.addEdge(1,2)
newGraph.addEdge(1,5)
newGraph.addEdge(1,3)
newGraph.addEdge(1,4)
newGraph.addEdge(1,6)
newGraph.addEdge(1,7)
newGraph.addEdge(1,8)
newGraph.addEdge(1,9)
newGraph.addEdge(2,7)
newGraph.addEdge(2,3)
newGraph.addEdge(3,4)
newGraph.addEdge(4,5)
newGraph.addEdge(5,6)
newGraph.addEdge(6,7)
newGraph.addEdge(6,8)
newGraph.addEdge(7,8)
newGraph.addEdge(8,9)
newGraph.addEdge(9,10)
newGraph.addEdge(5,2)
print "Finding adjacent vertices"
newGraph.findVertex(1)
newGraph.findVertex(2)
newGraph.findVertex(5)
newGraph.findVertex(9)
newGraph.findVertex(10)

