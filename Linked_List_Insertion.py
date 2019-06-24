class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,newNode):
        if self.head is None :
            self.head=newNode
        else:
            lastNode = self.head
            while True :
               if lastNode.next is None :
                break
               lastNode=lastNode.next
            lastNode.next=newNode
    def printlist(self):
        currentNode=self.head
        while True :
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode=currentNode.next

if __name__ == '__main__':
    llist = LinkedList()
    No_of_Node = int(input("Enter total Number of Node"))
    for i in range(1,No_of_Node+1):
        if i is 1:
            EnteredNode = Node(input("Enter {}st Node :".format(i)))
        elif i is 2 :
            EnteredNode = Node(input("Enter {}nd Node :".format(i)))
        elif i is 3 :
            EnteredNode = Node(input("Enter {}rd Node :".format(i)))
        else:
            EnteredNode = Node(input("Enter {}th Node :".format(i)))
        llist.insert(EnteredNode)
    llist.printlist()
